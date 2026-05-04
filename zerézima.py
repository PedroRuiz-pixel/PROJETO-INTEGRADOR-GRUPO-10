votos = []


def zerezima():
    votos.clear()

    for c in candidatos:
        c["votos"] = 0

    for e in eleitores:
        e["status"] = "Não votou"

    print("\n=== ZERÉZIMA ===")
    print("Todos os votos foram zerados.")
    print("Lista de candidatos com total de votos igual a zero:")

    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return

    for c in candidatos:
        print(f"Nome: {c['nome']} | Número: {c['numero']} | Partido: {c['partido']} | Votos: {c['votos']}")

    print("Zerézima realizada com sucesso!")
