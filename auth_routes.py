from fastapi import APIRouter,Depends
from models import Usuario
from dependencies import pegar_sessao
auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def home():
    """
    explicação, docString da api
    Docstring for autenticar
    """
    return{"mensagem":"fera","autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str,nome:str,session = Depends(pegar_sessao())):
    
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return{"menssagem":"ja existe um usuario com esse email"}
    else:
        novo_usuario = Usuario(nome,email,senha)    
        session.add(novo_usuario)
        session.commit()
        return{"menssagem":"cadastrado com sucesso"}
