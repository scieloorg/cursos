# coding: utf-8
import urllib
import json


API_URL = 'http://search.twitter.com/search.json?q=%23'
HASHTAG = 'scielo'

# pesquisando no Twitter pela hashtag
response = urllib.urlopen(API_URL + HASHTAG)

# transformando o JSON retornado em estruturas nativas do Python
tweets = json.loads(response.read())

# geração da saída HTML
html = u'<table>'

for tweet in tweets['results']:
    html += u'<tr>'
    html += u'<td><img src="' + tweet['profile_image_url'] + u'"/></td>'
    html += u'<td>' + tweet['from_user_name'] + u'</td>'
    html += u'<td>' + tweet['text'] + u'</td>'
    html += u'<td>' + tweet['created_at'] + u'</td>'
    html += u'</tr>'

html += '</table>'

# saída dos dados utilizando a codificação utf-8
print html.encode('utf-8')
