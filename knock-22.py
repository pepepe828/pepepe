#coding:shift-jis

import gzip
import json
import re
fname = 'jawiki-country.json.gz'


def ext_UK():

    with gzip.open(fname, 'rt',encoding='utf-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == '�C�M���X':
                return data_json['text']

    raise ValueError('�C�M���X�̋L����������Ȃ�')


# ���K�\���̃R���p�C��
pattern = re.compile(r'^.*\[\[Category:(.*?)(?:\|.*)*\]\].*$', re.MULTILINE + re.VERBOSE)

# ���o
result = re.findall(pattern,ext_UK())

# ���ʕ\��
for line in result:
    print(line)
    