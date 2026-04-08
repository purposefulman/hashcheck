#!/bin/bash
# Быстрая установка hashcheck

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Установка hashcheck...${NC}"

# Создаём директорию
mkdir -p ~/.local/bin

# Скачиваем скрипт
curl -sSL https://raw.githubusercontent.com/yourusername/hashcheck/main/hashcheck/main.py -o ~/.local/bin/hashcheck

# Делаем исполняемым
chmod +x ~/.local/bin/hashcheck

# Добавляем в PATH если нужно
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc 2>/dev/null || true
    echo -e "${GREEN}Добавлено ~/.local/bin в PATH${NC}"
fi

echo -e "${GREEN}✅ Установка завершена!${NC}"
echo -e "Используйте: ${GREEN}hashcheck --help${NC}"
echo -e "Перезагрузите терминал или выполните: ${GREEN}source ~/.bashrc${NC}"