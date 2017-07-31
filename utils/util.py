# _*_ coding: utf-8 _*_

from fuzzywuzzy import fuzz


def calc_entropy(records, entropy_fields=None):
    """
    计算records各个字段的熵, 并由高到低排序
    :param records: 
    :param entropy_fields: 参与计算熵的字段名列表
    :return: 
    """
    rec_cnt = len(records)
    if rec_cnt == 0:
        return []
    entropy = {}
    if entropy_fields is not None:

        for record in records:
            for field, value in record.items():
                if field in entropy_fields:
                    if field not in entropy:
                        entropy[field] = []
                    entropy[field].append(value)
    else:
        for record in records:
            for field, value in record.items():
                if field not in entropy:
                    entropy[field] = []
                entropy[field].append(value)
    for field, value in entropy.items():
        entropy[field] = 1.0 * len(set(value)) / rec_cnt
    return sorted(entropy.items(), key=lambda i: i[1], reverse=True)


def calc_sim(sent1, sent2):
    return fuzz.ratio(sent1, sent2)


def tounicode(text):
    if not isinstance(text, unicode):
        return text.decode('utf-8')
    return text


if __name__ == '__main__':
    print calc_sim('多久年检一次', '我的车几年一年检？')

    recs = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 3, 'c': 1},
        {'a': 2, 'b': 1, 'c': 3},
        {'a': 1, 'b': 3, 'c': 4},
        {'a': 1, 'b': 2, 'c': 2}
    ]

    print calc_entropy(recs)  # [('c', 0.8), ('b', 0.6), ('a', 0.4)]
    # print calc_entropy(recs, ['a', 'b'])  # [('b', 0.6), ('a', 0.4)]
