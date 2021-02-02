from io import open
import urllib3
import requests
import os
from requests import ReadTimeout, ConnectionError, ConnectTimeout
from requests.exceptions import MissingSchema

'''funcao para ler arquivo'''
def urls(file):
    url_list = open(file, 'r').readlines()
    for x in url_list:
        if x == '\n':
            x.replace('\n','')
    return url_list

'''funcao para montar barra de proogresso'''
def barra_progresso(qtd_total, qtd_atual):
    x = round(qtd_atual/qtd_total*100)
    barra = '|'
    vb = round((x/10))
    vf = 10 - vb
    for n in range(vb):
        barra = barra + '>'
    for n in range(vf):
        barra = barra + ' '
    return f'{barra}| {x}%'

'''variaveis de apoio'''
qtdtentaivas = 3
a = 1
st2 = {}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#montando o dicionario com as URLs
for url in urls(r'/home/eron/Documents/urls.txt'):
    apoio = url.replace("\n", "")
    st2[apoio] = []

#loop para validação da URL
while (qtdtentaivas > 0):
    #limpando tela
    os.system('clear') or None # no windows usar cls
    print('\n\nAguarde, Verificando...      ', barra_progresso(qtdtentaivas, a))
    print('\n')
    for k,v in st2.items():
        try:
            res = requests.get(k,timeout=3, verify=False)
            if res:
                st2[k] = list(dict.fromkeys(st2.get(k) + ['URL OK']))
            elif res.status_code == 401:
                st2[k] = list(dict.fromkeys(st2.get(k) + ['URL OK']))
            else:
                st2[k] =list(dict.fromkeys(st2.get(k) + [res.reason]))
        except ReadTimeout as e:
            print('\t' + k, e,'\n')
            st2[k] = list(dict.fromkeys(st2.get(k) + ['Timeout']))
        except ConnectionError as e:
            print('\t' + k, e)
            st2[k] = list(dict.fromkeys(st2.get(k) + ['ConnectionError']))
        except ConnectTimeout as e:
            print('\t' + k, e)
            st2[k] = list(dict.fromkeys(st2.get(k) + ['ConnectTimeout']))
        except MissingSchema as e:
            print('URL invalida identificada')
            st2[k] = list(dict.fromkeys(st2.get(k) + ['URL invalida']))

    a = a + 1
    if a==qtdtentaivas+1:
        qtdtentaivas=-1

for k,v in st2.items():
    print('\t' + k,' STATUS: ',v)
    print('\n\t-')
