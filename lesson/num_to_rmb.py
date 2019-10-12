"""
价格转人民币读法
"""


def change(zs, dw_arr):
    """
    处理数据
    :param zs:  需要处理的数据
    :param dw_arr: 单位
    :param zw_arr: 中文
    :return:
    """
    zw_arr = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')

    temp = ''
    index = 0
    for item in zs:
        # 中文
        zw = zw_arr[int(item)]
        # 单位
        dw = dw_arr[index - len(zs)]

        # 单位是不是元 省略单位
        if zw == zw_arr[0] and dw != dw_arr[-1]:
            dw = ''
            #  如果temp零结尾 设置zw为空字符串
            if temp.endswith(zw_arr[0]):
                zw = ''

        # 单位是元 省略零
        if zw == zw_arr[0] and dw == dw_arr[-1]:
            zw = ''

        temp = temp + zw + dw
        index += 1

    if temp.endswith(zw_arr[0] + dw_arr[-1]):
        temp = temp[0:temp.index(zw_arr[0])] + temp[-1]
    return temp


def parser(num: str):
    rmb_str = (
        ('仟', '佰', '拾', '亿', '仟', '佰', '拾', '万', '仟', '佰', '拾', '元'),
        ('角', '分')
    )

    num_arr = []

    try:
        num.index('.')
    except ValueError:
        # 不包括小数
        num_arr.append(num)
        pass
    else:
        num_arr = num.split('.')
        # 处理小数
        num_arr[1] = change(num_arr[1], rmb_str[1])

    # 处理整数
    num_arr[0] = change(num_arr[0], rmb_str[0])

    print(num_arr)

    return 1


num = '100001.08'
parser(num)
