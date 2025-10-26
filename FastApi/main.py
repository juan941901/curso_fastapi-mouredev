from fastapi import FastAPI
from routers import users, products, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Router de usuarios
app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint raíz
@app.get("/")
async def root():
    return {"message" : "¡Hola FastApi!" }

