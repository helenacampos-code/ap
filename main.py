from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class itens (BaseModel):
    lote: int
    item: int
    nome: str
    descritivo: str
    unid_de_medida: str
    quant_total: int

@app.post ("/enviar-json")
async def receber_dados(dados: itens):
    return {
        "status": "Sucesso", 
        "mensagem": f"JSON recebido: {itens.nome}
    }

    