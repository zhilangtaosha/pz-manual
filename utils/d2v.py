# _*_ coding: utf-8 _*_


import json
import urllib


def get_sim_score(sent1, sent2):
    score = -1
    url = 'http://112.126.81.218:7777/sim/?s1=%s&s2=%s' % (urllib.quote(sent1), urllib.quote(sent2))
    content = urllib.urlopen(url)
    sim_json = json.loads(content.read())
    if sim_json['code'] == 1:
        score = sim_json['data']['sim']
    return float(score)


if __name__ == '__main__':
    print get_sim_score('方向盘沉', '那个好')
