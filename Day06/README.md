Начать с установки модулей:
pip install -r requirements.txt

Создать базу данных:
psql -U postgres
create database rustam;
create user rustam with login password 'rustam';
\q

В каждом задании запускать сначала сервер, потом клиент:
python3 reporting_server.py
python3 reporting_client(версия).py [...]