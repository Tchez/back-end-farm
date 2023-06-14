def jogadorEntidade(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "nome": db_item["nome"],
        "idade": db_item["idade"],
        "time": db_item["time"],
    }


def listaJogadoresEntidade(db_items) -> list:
    return [jogadorEntidade(item) for item in db_items]
