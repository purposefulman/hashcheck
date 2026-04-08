.PHONY: install uninstall test clean help

PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin
PYTHON = python3

help:
	@echo "Доступные команды:"
	@echo "  make install   - Установить hashcheck"
	@echo "  make uninstall - Удалить hashcheck"
	@echo "  make test      - Запустить тесты"
	@echo "  make clean     - Очистить временные файлы"

install:
	@echo "Установка hashcheck..."
	@mkdir -p $(BINDIR)
	@cp hashcheck/main.py $(BINDIR)/hashcheck
	@chmod +x $(BINDIR)/hashcheck
	@echo "✅ Установка завершена. Используйте 'hashcheck --help'"

uninstall:
	@echo "Удаление hashcheck..."
	@rm -f $(BINDIR)/hashcheck
	@echo "✅ Удаление завершено"

test:
	@echo "Запуск тестов..."
	@$(PYTHON) -m pytest tests/ -v

clean:
	@echo "Очистка временных файлов..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@echo "✅ Очистка завершена"