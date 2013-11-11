# coding: utf-8
import urllib
import json

username = raw_input('Digite seu nome de usuário: ')
user_token = raw_input('Digite seu token de acesso: ')

API_URL = 'http://manager.scielo.org/api/v1/journals/?format=json&username=%s&api_key=%s&limit=0' % (username, user_token)

# acessando a lista de periódicos
response = urllib.urlopen(API_URL)

# transformando o JSON retornado em estruturas nativas do Python
journals = json.loads(response.read())

# geração da saída HTML
html = u'<table>'

for journal in journals['objects']:
    html += u'<tr>'
    html += u'<td>%s</td>' % journal['acronym']
    html += u'<td>%s</td>' % journal['short_title']
    html += u'<td>%s</td>' % journal['use_license']['license_code']
    html += u'<td>%s</td>' % ', '.join(journal['study_areas'])
    html += u'</tr>'

html += '</table>'

# saída dos dados utilizando a codificação utf-8
out = open('journals.html', 'w')
out.write(html.encode('utf-8'))
out.close()

