from fastapi import FastAPI
from routes import health

app = router

@app.get("/")
async def read_root():
    return {"Hello": "World"}
