# 基于txt文件构建字典,key是中文,value是对应的数字
import csv

csv_file = "out1.txt"  #好像utf-8不行


def row_csv2dict(csv_file):
    dict_club = {}
    with open(csv_file)as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            dict_club[row[0]] = row[1]
    return dict_club


word_dict = row_csv2dict(csv_file)


# 将所有value变成4位数字,如果是23,则转为"0023",然后保存为字典
def to4int(word_list):
    """
    :param word_list: dict word['汉子']='数字'
    :return 已经把数字标准化的字典
    """
    for (key, value) in word_list.items():
        if int(value) < 1000:
            word_list[key] = "%04d" % int(value)
    return word_list


word_dict = to4int(word_dict)

# 构建输入一句话,然后逐行输入word_list
sequence = "妈的智障"


def Sequence2List(sequence):
    """

    :param sequence: 输入字符串,比如"妈的智障"
    :return: 列表
    """
    word_list = []
    for _, word in enumerate(sequence):
        word_list.append(word_dict[word])
    return word_list


num_list = Sequence2List(sequence)
# e.g.['3992','6674','9204','1617']

#  根据数字列表来还原字符串
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


def List2Sequence(num_list, word_dict):
    string = []
    for num in num_list:
        string.append(get_key(word_dict, num)[0])
    sequence = "".join(string)
    return sequence

back=List2Sequence(num_list, word_dict)