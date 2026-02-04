from fastapi import FastAPI
from routes.health import router as health_router
from routes.login import router as login_router
app = FastAPI()
app.include_router(health_router)
app.include_router(login_router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Backend Developer Hub FastAPI!"}