from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Creación clase con BaseModel para manipulación de datos
# de la solicitud
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Creación de lista con valores para la clase, es importante
# recordar que se debe colocar el nombre dentro de la clase
# Para asignar el valor del mismo
users_list = [User(id=1, name="Juan", surname="David", url="kajubyte.com", age=31),
              User(id=2, name="maria", surname="camila", url="maxilusiones.com", age=30)]

# Instanciamos FastAPI
router = APIRouter()

# Endpoint de tipo get para devolver la lista de usuarios
@router.get("/get_users")
async def get_users():
    return users_list

# Endpoint de tipo get para devolver un usuario por id
# colocamos el id como parte del path
@router.get("/get_user/{id}")
async def get_user(id: int):
    # Filtramos la lista de usuarios por id
    user = filter(lambda user: user.id == id, users_list)
    try:
      # Devolvemos el primer elemento de la lista filtrada
      return list(user)[0]
    except:
      # Si no se encuentra el usuario, devolvemos un
      # diccionario vacío
      return {}
    
# Endpoint usando path de consulta para devolver un usuario
# por id, pero en ese caso usamos query parameters que es
# usar el signo de interrogación (?) para enviar datos
# y debemos colocar el mismo nombre del parámetro en la URL
# para este ejemplo es "id"
@router.get("/user_query/")
async def user_query(id: int):
    # Filtramos la lista de usuarios por id
    user = filter(lambda user: user.id == id, users_list)
    try:
      # Devolvemos el primer elemento de la lista filtrada
      return list(user)[0]
    except:
      # Si no se encuentra el usuario, devolvemos un
      # diccionario vacío
      return {}
    

# Endpoint para crear un usuario en el modelo, usando
# el método POST
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user

# Endpoint para actualizar un usuario en el modelo, usando
# el método PUT
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No se ha actualizado el usuario")

    return user

# Endpoint para eliminar un usuario en el modelo, usando
# el método DELETE
@router.delete("/user/{id}", status_code=204)
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No se ha eliminado el usuario")

# Devolvemos la lista de usuarios dentro del modelo
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
