# microservice_architecture

### Для построения микросервисной архитектура с помощью Docker и RabbitHQ. 

Этот проект использует RabbitMQ для обработки сообщений и Python для сбора метрик и визуализации ошибок. В этом README описаны шаги для настройки и запуска Docker-контейнеров, работы с метками ошибок и создания графиков.

1) Собираем образ:

```
docker-compose build
```
2) Запискаем сервисы. Эта команда запустит все сервисы, определенные в docker-compose.yml, включая RabbitMQ. Флаг -d запускает сервисы в фоновом режиме.:

```
docker-compose up -d
```
3) Проверяем логи:
```
docker-compose logs -f rabbitmq
```