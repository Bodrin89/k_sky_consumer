# Сервис приема чеков и аналитики

## Описание

---

Это второй сервис, который принимает сообщения в kafka, разбивает содержимое чеков на привязку к местам покупок, считает
аналитику и предоставляет данные по API. Раз в час производится пересчет аналитики.
Не аунтефицированые пользователи могут смотреть общую аналитику, пользователи с ролью "ADMIN" могут получать сумму 
всех чаевых за указанный период.

Для успешного приема сообщений в kafka необходимо запустить контейнер в первом сервисе.
Список не обходимых переменных окружения находится в .env.example

## Установка:

---

1. Клонируйте репозиторий с github на локальный компьютер
2. Создайте в корне проекта файл .env и заполните переменными окружения из .env.example
3. Соберите и поднимите docker-контейнер командой `docker-compose up -d --build`

+ ### SWAGGER: http://localhost:8002/docs/swagger

---
