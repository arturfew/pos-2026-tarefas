import json

with open("imobiliaria.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

imoveis = dados["imobiliaria"]["imoveis"]

while True:
    print("\n IMOBILIARIA ")
    for i, imovel in enumerate(imoveis):
        print(f"[{i+1}] {imovel['descricao'][:50]}...")
    print("[0] Sair")

    escolha = input("\n Digite o ID: ").strip()

    if escolha == "0":
        print("Encerrando. Ate logo!")
        break

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(imoveis):
        print("ID invalido! Tente novamente.")
        continue

    im = imoveis[int(escolha) - 1]
    p  = im["proprietario"]
    e  = im["endereco"]
    c  = im["caracteristicas"]

    print("\n" + "=" * 45)
    print("  DETALHES DO IMOVEL")
    print("=" * 45)
    print(f"  Descricao   : {im['descricao']}")
    print(f"  Valor       : {im['valor']}")
    print()
    print(f"  PROPRIETARIO")
    print(f"  Nome        : {p['nome']}")
    print(f"  Email       : {p['email'] or 'nao informado'}")
    if p["telefones"]:
        print(f"  Telefones   : {', '.join(p['telefones'])}")
    else:
        print(f"  Telefones   : nao informado")
    print()
    print(f"  ENDERECO")
    print(f"  Rua         : {e['rua']}")
    print(f"  Bairro      : {e['bairro']}")
    print(f"  Cidade      : {e['cidade']}")
    print(f"  Numero      : {e['numero'] if e['numero'] is not None else 'sem numero'}")
    print()
    print(f"  CARACTERISTICAS")
    print(f"  Tamanho     : {c['tamanho']}")
    print(f"  Quartos     : {c['numQuartos']}")
    print(f"  Banheiros   : {c['numBanheiros']}")
    print("=" * 45)