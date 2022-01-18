# fastapi-tutorial-aiosqlite

The FastAPI SQL database tutorial 

https://fastapi.tiangolo.com/tutorial/sql-databases/

modified to use `sqlite+aiosqlite` and real async calls.

Note that this demo uses the built-in async support in SQLAlchemy 1.4+ and does **not** need the [databases](https://pypi.org/project/databases/) module.

### How to run:

To launch uvicorn:

```
uvicorn sql_app.main:app --reload
```

Then load the fancy interactive docs page at

http://localhost:8000/docs
