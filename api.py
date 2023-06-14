from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jogador.routes import router as jogador_router

client_app = [
    "http://localhost:3000",
]

app = FastAPI()

app.include_router(jogador_router, tags=["jogador"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=client_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
