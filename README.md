# ts_hq
Короткое описание установки задания.
## Установка
1. Клонируйте репозиторий:
```bash
git clone [https://github.com/rastal88/ts_hq.git)https://github.com/rastal88/ts_hq.git]
```
2.Перейдите в директорию проекта:
```bash
cd ваша папка проекта
```
3.Создайте и активируйте виртуальное окружение
```bash
    python -m venv venv
    source venv/bin/activate
```
4.Переименуйте .env.example в .env и замените значения переменных на свои
5.Установите зависимости:  
```bash
pip install -r requirements.txt
```
6.Для запуска проекта воспользуйтесь Docker и docker-compose. Убедитесь, что у вас установлен Docker и docker-compose. Затем выполните команду:
```bash
docker-compose up
```
7.Запустите миграции:
```bash
docker-compose exec web python manage.py migrate
```
8.Запустите приложение:
теперь проект будет доступен по адресу http://localhost:8000/.

API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ
http://localhost:8000/api/lessons/
API с выведением списка уроков по конкретному продукту 
http://localhost:8000/api/lessons/product/<int:product_id>/
API для отображения статистики по продуктам
http://localhost:8000/api/lessons/products/stats/
