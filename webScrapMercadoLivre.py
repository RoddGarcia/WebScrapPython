# MERCADO LIVRE

import requests                                             # Fazer requisições
from bs4 import BeautifulSoup as bs                         # Resposta da requisição (HTML) e converter para um objeto, faremos buscas nele.
import os                                                   # Operações que envolvem o sistema/console.
import pandas as pd

lista = []

os.system('cls')                                            # Limpa console.
urlbase = 'https://lista.mercadolivre.com.br/'              # Será usado no request ++ input do produto.

produto = input('Produto: ')                                # Pergunta de qual produto o usuário quer procurar.

response = requests.get(urlbase+produto)                    # Pegar requests do site + produto.

site = bs(response.text, 'html.parser')                     # Colocar a resposta em texto html.parser

# print(site.prettify())                                       # Usar esse para analisar o HTML ou usar o Inspect elements no navegador.

produtos = site.findAll('li', attrs={'class': 'ui-search-layout__item'})                                          # As características do item, que serão quebradas logo em seguida:

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})                                         # Nome
    preco = produto.find('span', attrs={'class': 'price-tag-amount'})                                            # Preço
    link = produto.find('a', attrs={'class': 'ui-search-result__content ui-search-link'})                    # Link

    # print('Título do produto: ',titulo.text,'\nPreço: ',preco.text,'\nLink: ',link.text)
    print('Nome do produto:     ',titulo.text)
    print('Preço:   ',preco.text)
    print()
    print(link['href'])
    print()
    lista.append([titulo.text,preco.text,link['href']])                             # Adiciona cada item na lista "lista".

tabela = pd.DataFrame(lista, columns=['Produto','Preço','Link'])
tabela.to_excel('Produtos do MercadoLivre.xlsx',index=False)