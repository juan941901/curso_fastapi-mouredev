from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Creación clase con BaseModel para manipulación de datos
# de la solicitud
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool

# Creación de lista con valores para la clase, es importante
# recordar que se debe colocar el nombre dentro de la clase
# Para asignar el valor del mismo
products_list = [Product(id=1, name="Laptop", description="A high-end laptop", price=1500.00, in_stock=True),
                 Product(id=2, name="Smartphone", description="A latest model smartphone", price=800.00, in_stock=False)]

# Instanciamos FastAPI
router = APIRouter(
    prefix="/products", # Prefijo para todas las rutas en este router
    tags=["products"], # Etiquetas para la documentación
    responses={404: {"message": "No encontrado"}} # Respuestas personalizadas
)

# Endpoint de tipo get para devolver la lista de productos
@router.get("/get_products")
async def get_products():
    return products_list

# Endpoint de tipo get para devolver un producto por id
# colocamos el id como parte del path
@router.get("/get_product/{id}")
async def get_product(id: int):
    # Filtramos la lista de productos por id
    product = filter(lambda product: product.id == id, products_list)
    try:
      # Devolvemos el primer elemento de la lista filtrada
      return list(product)[0]
    except:
      # Si no se encuentra el producto, devolvemos un
      # diccionario vacío
      return {}