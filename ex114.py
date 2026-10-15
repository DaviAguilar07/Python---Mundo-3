import urllib.request
import urllib.error

try:
    urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site está indisponível no momento.')
else:
    print('O site está acessível.')
    