from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def ler_raiz():
    return{"mensage": "Minha primeira API está funcionando!"}