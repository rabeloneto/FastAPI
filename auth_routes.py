from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    explicação, docString da api
    Docstring for autenticar
    """
    return{"mensagem":"fera","autenticado":False}
