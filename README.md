# parsers_repositories


# RUN

1. Клонировать проект

```
$ https://github.com/LeonMaxwell/parsers_repositories.git
$ cd parsers_repositories
```

2. Запуск контейнера

```
$ docker-compose build
$ docker-compose up -d
```

3. Остановить контейнеры

```
$ docker-compose down
```

4. Запуск тестов

```
docker exec -it parsers_app pytest
```

5. Открыть документацию АПИ

```
http://0.0.0.0:7000/api/docs#
```