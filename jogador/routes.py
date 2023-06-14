from .model import Jogador
from .schemas import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId
from config.db import connection
from fastapi import APIRouter

router = APIRouter()


@router.get("/jogadores")
async def find_all_jogador():
    """Lista todos os jogadores"""
    jogadores = connection.local.jogador.find({})
    return listaJogadoresEntidade(jogadores)


@router.get("/jogadores/{jogador_id}")
async def find_jogador(jogador_id: str):
    """Busca jogador por id"""
    jogador = connection.local.jogador.find_one({"_id": ObjectId(jogador_id)})
    return jogadorEntidade(jogador)


@router.post("/jogadores")
async def create_jogador(jogador: Jogador):
    """Insere jogador"""
    jogador = dict(jogador)
    connection.local.jogador.insert_one(jogador)
    return listaJogadoresEntidade(connection.local.jogador.find({}))


@router.put("/jogadores/{jogador_id}")
async def update_jogador(jogador_id: str, jogador: Jogador):
    connection.local.jogador.find_one_and_update(
        {"_id": ObjectId(jogador_id)}, {"$set": dict(jogador)}
    )
    return jogadorEntidade(
        connection.local.jogador.find_one({"_id": ObjectId(jogador_id)})
    )


@router.delete("/jogadores/{jogador_id}")
async def delete_jogador(jogador_id: str):
    return jogadorEntidade(
        connection.local.jogador.find_one_and_delete({"_id": ObjectId(jogador_id)})
    )
