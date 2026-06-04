from fastapi import FastAPI

from app.routers import auth, users

app = FastAPI(title="fijipiji")

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
