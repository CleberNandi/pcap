from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1, nome="Playstation 5", preco=5745.55, em_oferta=True),
    Produto(id=2, nome="Nintendo Wii", preco=5265.1),
    Produto(id=3, nome="Xbox one Series", preco=4850.55),
    Produto(id=4, nome="Super Nintendo", preco=234.00, em_oferta=True),
    Produto(id=5, nome="Atari 2600", preco=200.00),
]

@app.get("/")
async def index():
    return {"Cleber": "Goulart Nandi"}

@app.get("/produtos/{id}")
async def buscar_produtos(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

@app.put("/produtos/{id}")
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None