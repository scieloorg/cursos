# coding: utf-8
import json

dados_json = """
{
    "nome": "Gustavo Fonseca",
    "idade": 28,
    "telefones": ["(11)99999999", "(11)88888888"]
}
"""

dados_dict = json.loads(dados_json)

print dados_dict
print u'Meu nome é', dados_dict['nome']
