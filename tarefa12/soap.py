import requests
import re

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

codigo = input("Digite o código do pais ").strip().upper()
operacao = input("1 - código de telefone, 2 - moeda, 3 - nome do país: ")

if operacao == "1":
    funcao = "CountryIntPhoneCode"
elif operacao == "2":
    funcao = "CountryCurrency"
elif operacao == "3":
    funcao = "CountryName"
else:
    print("Inválido!")
    exit()

payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>{codigo}</sCountryISOCode>
        </{funcao}>
    </soap:Body>
</soap:Envelope>"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    if operacao == "2":
        
        iso = re.search(r"<m:sISOCode>(.*?)</m:sISOCode>", response.text)
        nome = re.search(r"<m:sName>(.*?)</m:sName>", response.text)
        if iso and nome:
            print(f"Moeda: {nome.group(1)} ({iso.group(1)})")
        else:
            print("Nenhum resultado encontrado.")
    else:
        tag = f"{funcao}Result"
        match = re.search(rf"<m:{tag}>(.*?)</m:{tag}>", response.text)
        if match:
            print(f"Resultado: {match.group(1)}")
        else:
            print("Nenhum resultado encontrado.")
else:
    print(f"Erro na requisição: {response.status_code}")