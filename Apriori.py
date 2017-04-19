# -*- coding:gb2312 -*-
from json import dumps
from itertools import combinations

# Associate Algorithm
# 支持度 sup X项集和Y项集同时出现在集合D中次数 / 交易集合的总次数
# 置信度conf X项集和Y项集同时出现在集合D中次数 / X项集在D中出现的次数
# 增益度lift confidence(X -> Y) / P(Y)
# 强关联规则 最小支持度和最小置信度都是50%


# 从命令行读入关联项
def data_io():
    print("输入大写英文字母表示关联项，\n"
          "不同的项用空格分割，每行输入一个记录\n"
          "输入pass结束输入：\n")

    all_input = []

    while True:
        input_value = input("\n")
        if input_value in ['pass', 'pass\n', "Pass", "PASS"]:
            return all_input
        else:
            all_input.append(input_value)


# 把关联项的string解析成list
def parse_list(i_string):
    # 去除空格 去除重复项 拆分成数组
    raw_list = list(set(i_string.replace(" ", "")))
    return [str(item) for item in raw_list]


# 找出所有的频繁项集，这些项集每一个出现的频繁性至少大于等于min_sup
def find_freq_items(ori_set, i_list, m_sup):
    # 生成每个项出现的次数
    i_dict = {}
    for i in i_list:
        for item in i:
            if item in i_dict.keys():
                i_dict[item] = i_dict.get(item)+1
            else:
                i_dict[item] = 1
    # 删除非频繁项
    freq_i_dict = {}
    for k, v in i_dict.items():
        if v >= m_sup:
            freq_i_dict[k] = v

    return freq_i_dict


# 计算支持度dict
def get_sup_dict(ori_data, i_list):
    # 计算项集出现的次数
    appear_dict = {}
    for item in i_list:
        # 遍历项集的每一项 & 遍历数据集的每一项
        for v in ori_data:
            # 如果项集的数据集中出现过，就增加该项集出现的次数
            if set(list(item)).issubset(set(list(v))):
                if item in appear_dict.keys():
                    appear_dict[item] = appear_dict.get(item)+1
                else:
                    appear_dict[item] = 1

    # 计算项集的支持度
    total_appear = len(ori_data)
    s_dict = {}
    for k, v in appear_dict.items():
        s_dict[k] = v/total_appear

    return s_dict

# 频繁项挖掘
if __name__ == '__main__':
    # 设置最小支持度和最小置信度
    min_sup = 0.5
    min_conf = 0.5

    # 测试数据集
    item_string_list = ["A C D", "B C E", "A B C E", "B E"]

    # 解析数据集，例如 [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
    data_list = [parse_list(item) for item in item_string_list]

    # 项数
    item_num = 1

    # 项集初始化 例如 ['1', '2', '3', '4', '5']
    item_list = sorted(set([item for sub_list in data_list for item in sub_list]))

    # 迭代计算k项集
    while len(item_list) > 1:

        print("%d项集的值为" % item_num, item_list)

        # 计算支持度 例如 {'1': 0.5, '2': 0.75, '3': 0.75, '4': 0.25, '5': 0.75}
        sup_dict = get_sup_dict(data_list, item_list)
        print("%d项集的支持度为" % item_num, sup_dict)

        # 删除非频繁项
        for key, value in sup_dict.items():
            if value < min_sup:
                item_list.remove(key)
        print("剔除非频繁项集后，%d项集的值为" % item_num, item_list)

        # 计算频繁k+1项集
        item_num += 1
        # 根据保留的项集和k值计算排列组合
        item_list = sorted(set([item for sub_list in item_list for item in list(sub_list)]))
        item_list = list(combinations(item_list, item_num))

        print("\n")
