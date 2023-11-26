from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Данные о вас: Швецов Кирилл Николаевич"}


@app.get("/users")
async def users():
    return {"message": "Контактные данные: 7913263242"}


@app.get("/tools")
async def tools():
    return {"message": "Данные о вас: HTMl,CSS,SCSS,JS,TypeScript,Angular,rxjs,git"}
