# hashcheck-cli 🔐

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Утилита для проверки хэш-сумм файлов, в будущем планируется сделать графический интерфейс :) 


## ✨ Возможности

- Поддержка 7 алгоритмов хэширования:
  - `md5`, `sha1`, `sha256`, `sha512`
  - `sha3-256`, `sha3-512`, `blake2b`
- Проверка отдельных файлов
- Проверка по файлам контрольных сумм (как в `sha256sum`)
- Интерактивный режим
- Автоматическое определение алгоритма по длине хэша
- Красивый вывод с эмодзи ✅/❌

## 🚀 Быстрая установка

### python
``` bash
pip install hashcheck
```

### github
```bash
git clone https://github.com/yourusername/hashcheck.git
cd hashcheck
sudo make install
```

### cmd
```bash
curl -sSL https://raw.githubusercontent.com/yourusername/hashcheck/main/scripts/install.sh | bash
```

## 📖 Использование

### Базовые команды
#### Вычислить SHA256 файла
hashcheck yourfile.iso sha256

#### Проверить с ожидаемой суммой
hashcheck yourfile.iso sha256 -e "hash"

#### Проверить MD5
hashcheck file.bin md5

#### Проверить SHA512
hashcheck file.bin sha512

### Проверка по файлу контрольных сумм
```bash
# Создайте файл checksums.txt:
# e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  archlinux.iso

# Проверить все файлы
hashcheck -c checksums.txt

# Указать алгоритм явно
hashcheck -c checksums.txt sha256
```
### Интерактивный режим
```bash
hashcheck -i
```

## 🛠 Разработка
### Запуск из исходников
```bash
git clone https://github.com/yourusername/hashcheck.git
cd hashcheck
python3 -m hashcheck.main --help
```
### Запуск тестов
```bash
make test
```

## 📝 Примеры
### Пример 1: Проверка ISO образа Arch Linux
```bash
# Скачиваем ISO
wget https://archlinux.org/iso/latest/archlinux-x86_64.iso

# Скачиваем контрольную сумму
wget https://archlinux.org/iso/latest/sha256sums.txt

# Проверяем
hashcheck -c sha256sums.txt
```

### Пример 2: Проверка нескольких файлов
```bash
# Создаём файл с суммами
sha256sum file1.bin file2.bin > checksums.txt

# Проверяем
hashcheck -c checksums.txt
```

### Пример 3: В скриптах
```bash
#!/bin/bash
if hashcheck myfile.iso sha256 -e "expected_hash"; then
    echo "Файл валидный"
else
    echo "Файл повреждён"
fi
```

## 🤝 Вклад в проект
Приветствуются pull requests! Для крупных изменений, пожалуйста, сначала откройте issue.

Форкните репозиторий

Создайте ветку для фичи (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте ветку (git push origin feature/amazing-feature)

Откройте Pull Request

## 📄 Лицензия
Распространяется под лицензией MIT. Смотрите файл LICENSE для подробностей.

## 📞 Контакты
GitHub Issues: https://github.com/yourusername/hashcheck/issues

Email: viktor_freelance@proton.me