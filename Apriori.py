# -*- coding:gb2312 -*-
from json import dumps
from itertools import combinations

# Associate Algorithm
# ֧�ֶ� sup X���Y�ͬʱ�����ڼ���D�д��� / ���׼��ϵ��ܴ���
# ���Ŷ�conf X���Y�ͬʱ�����ڼ���D�д��� / X���D�г��ֵĴ���
# �����lift confidence(X -> Y) / P(Y)
# ǿ�������� ��С֧�ֶȺ���С���Ŷȶ���50%


# �������ж��������
def data_io():
    print("�����дӢ����ĸ��ʾ�����\n"
          "��ͬ�����ÿո�ָÿ������һ����¼\n"
          "����pass�������룺\n")

    all_input = []

    while True:
        input_value = input("\n")
        if input_value in ['pass', 'pass\n', "Pass", "PASS"]:
            return all_input
        else:
            all_input.append(input_value)


# �ѹ������string������list
def parse_list(i_string):
    # ȥ���ո� ȥ���ظ��� ��ֳ�����
    raw_list = list(set(i_string.replace(" ", "")))
    return [str(item) for item in raw_list]


# �ҳ����е�Ƶ�������Щ�ÿһ�����ֵ�Ƶ�������ٴ��ڵ���min_sup
def find_freq_items(ori_set, i_list, m_sup):
    # ����ÿ������ֵĴ���
    i_dict = {}
    for i in i_list:
        for item in i:
            if item in i_dict.keys():
                i_dict[item] = i_dict.get(item)+1
            else:
                i_dict[item] = 1
    # ɾ����Ƶ����
    freq_i_dict = {}
    for k, v in i_dict.items():
        if v >= m_sup:
            freq_i_dict[k] = v

    return freq_i_dict


# ����֧�ֶ�dict
def get_sup_dict(ori_data, i_list):
    # ��������ֵĴ���
    appear_dict = {}
    for item in i_list:
        # �������ÿһ�� & �������ݼ���ÿһ��
        for v in ori_data:
            # ���������ݼ��г��ֹ��������Ӹ�����ֵĴ���
            if set(list(item)).issubset(set(list(v))):
                if item in appear_dict.keys():
                    appear_dict[item] = appear_dict.get(item)+1
                else:
                    appear_dict[item] = 1

    # �������֧�ֶ�
    total_appear = len(ori_data)
    s_dict = {}
    for k, v in appear_dict.items():
        s_dict[k] = v/total_appear

    return s_dict

# Ƶ�����ھ�
if __name__ == '__main__':
    # ������С֧�ֶȺ���С���Ŷ�
    min_sup = 0.5
    min_conf = 0.5

    # �������ݼ�
    item_string_list = ["A C D", "B C E", "A B C E", "B E"]

    # �������ݼ������� [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
    data_list = [parse_list(item) for item in item_string_list]

    # ����
    item_num = 1

    # ���ʼ�� ���� ['1', '2', '3', '4', '5']
    item_list = sorted(set([item for sub_list in data_list for item in sub_list]))

    # ��������k�
    while len(item_list) > 1:

        print("%d���ֵΪ" % item_num, item_list)

        # ����֧�ֶ� ���� {'1': 0.5, '2': 0.75, '3': 0.75, '4': 0.25, '5': 0.75}
        sup_dict = get_sup_dict(data_list, item_list)
        print("%d���֧�ֶ�Ϊ" % item_num, sup_dict)

        # ɾ����Ƶ����
        for key, value in sup_dict.items():
            if value < min_sup:
                item_list.remove(key)
        print("�޳���Ƶ�����%d���ֵΪ" % item_num, item_list)

        # ����Ƶ��k+1�
        item_num += 1
        # ���ݱ��������kֵ�����������
        item_list = sorted(set([item for sub_list in item_list for item in list(sub_list)]))
        item_list = list(combinations(item_list, item_num))

        print("\n")
