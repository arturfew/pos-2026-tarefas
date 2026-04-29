import xml.dom.minidom
import json

def pega_texto(imovel, tag):
    els = imovel.getElementsByTagName(tag)
    if len(els) == 0:
        return None
    filho = els[0].firstChild
    if filho is None:
        return None
    return filho.nodeValue.strip()

dom = xml.dom.minidom.parse("imobiliaria.xml")
imoveis_xml = dom.getElementsByTagName("imovel")

imoveis = []

for imovel in imoveis_xml:

    
    telefones = []
    for t in imovel.getElementsByTagName("telefone"):
        telefones.append(t.firstChild.nodeValue.strip())

    
    numero_texto = pega_texto(imovel, "numero")
    if numero_texto is not None:
        numero = int(numero_texto)
    else:
        numero = None

    imoveis.append({
        "descricao": pega_texto(imovel, "descricao"),
        "proprietario": {
            "nome": pega_texto(imovel, "nome"),
            "email": pega_texto(imovel, "email"),
            "telefones": telefones
        },
        "endereco": {
            "rua": pega_texto(imovel, "rua"),
            "bairro": pega_texto(imovel, "bairro"),
            "cidade": pega_texto(imovel, "cidade"),
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": pega_texto(imovel, "tamanho"),
            "numQuartos": int(pega_texto(imovel, "numQuartos")),
            "numBanheiros": int(pega_texto(imovel, "numBanheiros"))
        },
        "valor": pega_texto(imovel, "valor")
    })

resultado = {"imobiliaria": {"imoveis": imoveis}}

with open("imobiliaria.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)

print("Arquivo imobiliaria.json criado com sucesso!")