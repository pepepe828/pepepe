#coding:shift-jis
import json
import gzip

fname = 'jawiki-country.json.gz'

def ext():
    with gzip.open(fname , mode='rt',encoding='utf-8') as f:
        for line in f:
            data_json = json.loads(line)
            if data_json['title'] == '�C�M���X' :
                return data_jason['text']


#�J�e�S���������s�̒��o

pattern = re.compile(r'^(\[\[Category:.*]])$',re.MULTILINE + re.VERBOSE)

result = re.findall(pattern,ext())
for line in result:
    print (line)