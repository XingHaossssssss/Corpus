import requests
import time
import uuid
import hashlib
import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

def fanyi1(word):

    data = {}
    data['i'] = word
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15613765644784'
    data['sign'] = '5caabbf646f6585277b7cebf45f18244'
    data['ts'] = '1561376564478'
    data['bv'] = '6074bfcb52fb292f0428cb1dd669cfb8'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')

    r = urllib.request.urlopen(url, data)
    html = r.read().decode('utf-8')

    target = json.loads(html)

    try:
        result = target['translateResult'][0][0]['tgt']
    except:
        result = 'Translate failed'
    return result






