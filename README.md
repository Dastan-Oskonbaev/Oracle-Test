# Название Проекта

API для получения погоды в любом городе 

## Установка

1. Откройте терминал, перейдите в необходимую вам директорию,
например: 

cd Desktop/

2. Склонируйте репозиторий:

   git clone https://github.com/Dastan-Oskonbaev/Oracle-Test.git

3. Перейдите в директорию с проектом:

   cd Oracle-Test
   
4. Создайте виртуальное окружение:

python -m venv venv

5. Активируйте его:

source venv/bin/activate  
# Для Windows: venv\Scripts\activate

6. Установите зависимости:

pip install -r requirements.txt

7. Запустите проект с использованием Docker Compose:

docker-compose up

При необходимости, вы можете использовать флаг -d для запуска в фоновом режиме.

Приложение будет доступно по адресу http://localhost:8000/.

