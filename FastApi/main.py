from fastapi import FastAPI
from routers import users, products
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Router de usuarios
app.include_router(users.router)
app.include_router(products.router)

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint raíz
@app.get("/")
async def root():
    return {"message" : "¡Hola FastApi!" }

