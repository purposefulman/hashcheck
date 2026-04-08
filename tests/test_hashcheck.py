#!/usr/bin/env python3
import unittest
import tempfile
import os
import hashlib
from pathlib import Path
import sys

# Добавляем путь к модулю
sys.path.insert(0, str(Path(__file__).parent.parent))

from hashcheck.main import calculate_hash, check_single_file

class TestHashCheck(unittest.TestCase):
    def setUp(self):
        # Создаём временный файл для тестов
        self.temp_file = tempfile.NamedTemporaryFile(mode='wb', delete=False)
        self.test_data = b"Hello, World!"
        self.temp_file.write(self.test_data)
        self.temp_file.close()
        self.file_path = self.temp_file.name
    
    def tearDown(self):
        # Удаляем временный файл
        os.unlink(self.file_path)
    
    def test_calculate_hash_md5(self):
        expected = hashlib.md5(self.test_data).hexdigest()
        result = calculate_hash(self.file_path, 'md5')
        self.assertEqual(result, expected)
    
    def test_calculate_hash_sha256(self):
        expected = hashlib.sha256(self.test_data).hexdigest()
        result = calculate_hash(self.file_path, 'sha256')
        self.assertEqual(result, expected)
    
    def test_calculate_hash_sha512(self):
        expected = hashlib.sha512(self.test_data).hexdigest()
        result = calculate_hash(self.file_path, 'sha512')
        self.assertEqual(result, expected)
    
    def test_nonexistent_file(self):
        result = calculate_hash('/nonexistent/file.txt', 'sha256')
        self.assertIsNone(result)
    
    def test_invalid_algorithm(self):
        result = calculate_hash(self.file_path, 'invalid_algo')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()