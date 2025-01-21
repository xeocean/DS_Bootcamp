#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

# 1. Создание и активация виртуального окружения
if [ ! -d ".env" ]; then
    python3 -m venv .env
    echo -e "${GREEN}Virtual environment created.${NC}"
else
    echo -e "${YELLOW}Virtual environment already exists.${NC}"
fi

source .env/bin/activate
echo -e "${BLUE}Virtual environment activated.${NC}"

# 2. Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}Dependencies installed.${NC}"

# 3. Запуск тестов
pytest tests/tests_run.py
echo -e "${GREEN}Tests executed successfully.${NC}"

# # 4. Проверка наличия Docker
# if command -v docker &> /dev/null; then
#     echo -e "${BLUE}Docker is installed. Proceeding with container creation.${NC}"
    
#     docker build -t movielens-analysis .
#     echo -e "${GREEN}Docker image created.${NC}"

#     docker run -p 8888:8888 movielens-analysis
#     echo -e "${GREEN}Docker container is running.${NC}"
# else
#     echo -e "${RED}Docker is not installed. Skipping container creation.${NC}"
# fi
