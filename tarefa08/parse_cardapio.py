import xml.dom.minidom

dom = xml.dom.minidom.parse("cardapio.xml")
pratos = dom.getElementsByTagName("prato")


print("=== CARDAPIO ===")
for prato in pratos:
    id = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f"[{id}] {nome}")

escolha = input("\nDigite o ID do prato: ").upper()


for prato in pratos:
    if prato.getAttribute("id") == escolha:
        nome      = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        preco     = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
        calorias  = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
        tempo     = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue

        ingredientes = prato.getElementsByTagName("ingrediente")

        print(f"\nNome: {nome}")
        print(f"Descricao: {descricao}")
        print("Ingredientes:")
        for i in ingredientes:
            print(f"  - {i.firstChild.nodeValue}")
        print(f"Preco: {preco}")
        print(f"Calorias: {calorias}")
        print(f"Tempo de preparo: {tempo}")