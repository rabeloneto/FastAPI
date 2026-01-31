from fastapi import FastAPI
#para roda: uvicorn main:app --reload
#.venv\Scripts\activate 
#sair deactivate
app = FastAPI()
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
