# Extralogic test app

- **Frontend:**
    - Deploy: [form-constructor-react](https://form-constructor-react.herokuapp.com/)
    - GitHub: [form-constructor-fronend](https://github.com/Goradii/form-constructor-fronend)
    - React.TS
    - Пример формы

- **Backend:**
    - Deploy: [test-app-for-extralogic](https://test-app-for-extralogic.herokuapp.com/)
    - GitHub: [form-constructor-backend](https://github.com/Goradii/form-constructor-backend)
    - Python
    - FastAPI(fastapi-jsonrpc)
    - SqlAlchemy(asyncpg)
    - PostgreSql

* * *

## Описание работы

В ТЗ для меня было много неоднозначных и непонятных моментов, так что я принял решение переосмыслить задачу, оставив при этом основные моменты.
Важными для исполнения я выделил 3 пункта:
- Создание приложения на Python
- Создание прототипа приложения - Конструктор форм
- Реализовать взаимодействие двух приложений по протоколу json-rpc

Однако вместо горизонтальной декомпозиции проекта, я применил вертикальную. И выделил Frontend приложение на React TypeScript  и Backend приложение на FastAPI Python.

 * * *

## Выбор стека

- **React TypeScript**
    - Я не считаю себя достаточно опытным Frontend разработчиком, поэтому пропущу свои решения в этой области
- **FastAPI Python**
    - Поскольку я первый раз столкнулся с задачей реализации протокола json-rpc, я задал нашел несколько репозиториев на gihub.
        - ❌ django-json-rpc:  Репозиторий обновлялся 6 лет назад
        - ☑️ flask-jsonrpc:  Живой репозиторий
        - ✅ fastapi-jsonrpc:  Живой репозиторий. FastAPI предоставляет OpenAPI/Swagger и валидацию данных Pydantic из коробки
    - SqlAlchemy просто стандартный ORM для Python. Я не стал использовать NoSQL базы только для того что бы использовать SqlAlchemy в приложении.
    - PostgreSql  так же как и алхимия стандартный выбор для Python проeктов.
