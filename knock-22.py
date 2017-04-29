#coding:shift-jis

import gzip
import json
import re
fname = 'jawiki-country.json.gz'


def ext_UK():

    with gzip.open(fname, 'rt',encoding='utf-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


# 正規表現のコンパイル
pattern = re.compile(r'^.*\[\[Category:(.*?)(?:\|.*)*\]\].*$', re.MULTILINE + re.VERBOSE)

# 抽出
result = re.findall(pattern,ext_UK())

# 結果表示
for line in result:
    print(line)
    