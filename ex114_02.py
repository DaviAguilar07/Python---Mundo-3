import urllib.request
import urllib.error

try:
    resposta = urllib.request.urlopen("https://www.pudim.com.br", timeout=10)
    print(f"Site acessível! Status: {resposta.status}")

except urllib.error.HTTPError as e:
    print(f"Erro HTTP: {e.code}")

except urllib.error.URLError as e:
    print(f"Erro de conexão: {e.reason}")

except Exception as e:
    print(f"Erro inesperado: {e}")
    