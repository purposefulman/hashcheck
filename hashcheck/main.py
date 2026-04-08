#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hashcheck - Утилита для проверки хэш-сумм файлов
Поддерживает: sha256, sha512, sha1, md5, sha3-256, sha3-512, blake2b
"""

import hashlib
import sys
import os
import argparse
from pathlib import Path
from typing import Dict, Callable, Optional

# Доступные алгоритмы хэширования
HASH_ALGORITHMS: Dict[str, Callable] = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
    'sha3-256': hashlib.sha3_256,
    'sha3-512': hashlib.sha3_512,
    'blake2b': hashlib.blake2b,
}

def calculate_hash(file_path: str, algorithm: str, buffer_size: int = 65536) -> Optional[str]:
    """Вычисляет хэш-сумму файла"""
    if algorithm not in HASH_ALGORITHMS:
        print(f"Ошибка: Неподдерживаемый алгоритм '{algorithm}'", file=sys.stderr)
        return None
    
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден", file=sys.stderr)
        return None
    
    try:
        hash_func = HASH_ALGORITHMS[algorithm]()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(buffer_size), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except PermissionError:
        print(f"Ошибка: Нет доступа к файлу '{file_path}'", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_path}': {e}", file=sys.stderr)
        return None

def check_single_file(file_path: str, algorithm: str, expected_hash: Optional[str] = None):
    """Проверяет один файл"""
    calculated = calculate_hash(file_path, algorithm)
    
    if calculated is None:
        return False
    
    print(f"Файл: {file_path}")
    print(f"Алгоритм: {algorithm.upper()}")
    print(f"Хэш: {calculated}")
    
    if expected_hash:
        if calculated.lower() == expected_hash.lower():
            print("✅ Хэш совпадает с ожидаемым!")
            return True
        else:
            print("❌ Хэш НЕ совпадает с ожидаемым!")
            print(f"Ожидалось: {expected_hash}")
            return False
    
    return True

def check_from_checksum_file(checksum_file: str, algorithm: Optional[str] = None):
    """Проверяет файлы по файлу с хэш-суммами"""
    if not os.path.exists(checksum_file):
        print(f"Ошибка: Файл с контрольными суммами '{checksum_file}' не найден", file=sys.stderr)
        return False
    
    errors = 0
    total = 0
    
    with open(checksum_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split()
            if len(parts) < 2:
                print(f"Предупреждение: Неверный формат в строке {line_num}: '{line}'", file=sys.stderr)
                continue
            
            file_hash = parts[0]
            file_name = parts[1].lstrip('*').lstrip(' ')
            
            if algorithm:
                current_algo = algorithm
            else:
                hash_len = len(file_hash)
                if hash_len == 32:
                    current_algo = 'md5'
                elif hash_len == 40:
                    current_algo = 'sha1'
                elif hash_len == 64:
                    current_algo = 'sha256'
                elif hash_len == 128:
                    current_algo = 'sha512'
                else:
                    print(f"Предупреждение: Не могу определить алгоритм для строки {line_num}", file=sys.stderr)
                    continue
            
            calculated = calculate_hash(file_name, current_algo)
            total += 1
            
            if calculated:
                if calculated.lower() == file_hash.lower():
                    print(f"✅ {file_name}: OK")
                else:
                    print(f"❌ {file_name}: FAILED")
                    errors += 1
            else:
                errors += 1
    
    print(f"\nПроверено файлов: {total}")
    if errors == 0:
        print("✅ Все проверки пройдены успешно!")
        return True
    else:
        print(f"❌ Ошибок: {errors}")
        return False

def interactive_mode():
    """Интерактивный режим"""
    print("=" * 60)
    print("  hashcheck - Интерактивный режим")
    print("=" * 60)
    
    print("\nДоступные алгоритмы:")
    for i, algo in enumerate(HASH_ALGORITHMS.keys(), 1):
        print(f"  {i}. {algo.upper()}")
    
    while True:
        try:
            choice = input(f"\nВыберите алгоритм (1-{len(HASH_ALGORITHMS)}) или введите название: ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(HASH_ALGORITHMS):
                    algorithm = list(HASH_ALGORITHMS.keys())[idx]
                    break
            elif choice.lower() in HASH_ALGORITHMS:
                algorithm = choice.lower()
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except KeyboardInterrupt:
            print("\nВыход...")
            sys.exit(0)
    
    print("\nРежимы работы:")
    print("  1. Вычислить хэш файла")
    print("  2. Сравнить с ожидаемой хэш-суммой")
    print("  3. Проверить по файлу контрольных сумм")
    
    mode = input("\nВыберите режим (1-3): ").strip()
    
    if mode == '1':
        file_path = input("Путь к файлу: ").strip()
        check_single_file(file_path, algorithm)
    elif mode == '2':
        file_path = input("Путь к файлу: ").strip()
        expected = input("Ожидаемая хэш-сумма: ").strip()
        check_single_file(file_path, algorithm, expected)
    elif mode == '3':
        checksum_file = input("Путь к файлу с контрольными суммами: ").strip()
        check_from_checksum_file(checksum_file, algorithm)
    else:
        print("Неверный режим")

def main():
    parser = argparse.ArgumentParser(
        description='Проверка файлов с различными хэш-суммами',
        epilog='Примеры:\n'
               '  hashcheck archlinux.iso sha256\n'
               '  hashcheck archlinux.iso sha256 -e a1b2c3...\n'
               '  hashcheck -c checksums.txt\n'
               '  hashcheck -i',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('file', nargs='?', help='Файл для проверки')
    parser.add_argument('algorithm', nargs='?', 
                       choices=list(HASH_ALGORITHMS.keys()),
                       help='Алгоритм хэширования')
    parser.add_argument('-e', '--expected', help='Ожидаемая хэш-сумма')
    parser.add_argument('-c', '--check', help='Файл с контрольными суммами для проверки')
    parser.add_argument('-i', '--interactive', action='store_true', help='Интерактивный режим')
    parser.add_argument('-v', '--version', action='version', version='hashcheck 1.0.0')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
        sys.exit(0)
    
    if args.check:
        success = check_from_checksum_file(args.check, args.algorithm)
        sys.exit(0 if success else 1)
    
    if not args.file or not args.algorithm:
        parser.print_help()
        sys.exit(1)
    
    success = check_single_file(args.file, args.algorithm, args.expected)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()