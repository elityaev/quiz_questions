# Quiz question


## Описание
Веб-сервис, выполняющий следующие функции:
   * принимает на вход POST-запросы с содержимым вида {"questions_num": integer};
   * с публичного сервиса с вопросами для викторин (https://jservice.io)
   запрашивает указанное в POST-запросе количество вопросов;
   * полученные уникальные вопросы с сопутствующей информацией (id вопроса, текст вопроса,
   ответ, дата создания вопроса) сохраняются в БД. Если полученный вопрос уже имеется
   в БД, вместо него запрашивается новый, пока не будет получен уникальный для БД вопрос;
   * в ответ на POST-запрос пользователю возвращается предыдущий (последний) сохраненный
   вопрос для викторины. В случае его отсутствия - пустой объект.  
 

## Использованные технологии

- [Python](https://docs.python.org/release/3.10.9/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/docs/) 
- [Sqlalchemy](https://docs.sqlalchemy.org/en/20/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://docs.docker.com/)

## Инструкция по запуску проекта 

1. Клонировать репозиторий.
    
    ```bash
    git clone git@github.com:elityaev/quiz_questions.git
    ```
    
2. Перейти в папку проекта и запустить проект в контейнерах:   
    ```bash
    сd quiz_questions/
    docker-compose up -d
    ```
3. Чтобы остановить работу приложения, необходимо выполнить команду:
   ```bash
    docker-compose stop
    ```

## Использование 

Взаимодействовать с сервисом можно через 
* Swagger, в котором задокументированы возможности API и пример запроса, перейдя по адресу http://127.0.0.1:8000/docs
* [Postman](https://www.postman.com/) - сервис для создания, тестирования, документирования, публикации и обслуживания API

### Пример запроса через командную строку
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question_num": 3
}'
```

### Пример ответа

```json
{
  "question_id": 151505,
  "text": "This resort chain is \"The antidote for civilization\"",
  "answer": "Club Med",
  "created_at": "2022-12-30T20:37:40.654000"
}
```
____

**Автор**

_Литяев Евгений_

