# coding: utf-8
import json

dados_json = open('dados.json')

dados_dict = json.load(dados_json)

print dados_dict
print u'Meu nome é', dados_dict['nome']
