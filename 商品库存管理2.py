# 假设文件中的数据按照这样来写：蓝莓，10,20（一行的数据）
import re


def read_goods(fn):
    fdic = {}
    with open(fn, "r") as f:
        for i in f.readlines():
            goodl = list(re.split(r"[,，]", i))
            goodl = [x.strip() for x in goodl]
            fdic[goodl[0]] = goodl
    return fdic


def add_goods(fdic, fn):
    goods_list = list(re.split('[,，]', input("请输入商品信息（商品名称，单价，数量），直接输入回车退出:")))
    if goods_list[0] == "":
        return 0
    elif len(goods_list) == 3:
        try:
            a = eval(goods_list[1]) + eval(goods_list[2])  # 防止输入价格时输入非数字符号
        except NameError:
            print("价格请输入数字符号")
        else:
            if goods_list[0] in fdic.keys():
                print("该商品已存在")
            else:
                fdic[goods_list[0]] = goods_list
                with open(fn, "a") as f:
                    f.writelines(','.join(goods_list))
                    f.write("\n")
            add_goods(fdic, fn)
    else:
        if goods_list[0] in fdic.keys():
            print("该商品已存在")
        else:
            print("输入错误请重新输入")
        add_goods(fdic, fn)


def find_goods(fdic):
    while True:
        good_name = input("请输入查询商品名称，直接输入回车退出：")
        if good_name == "":
            break
        else:
            for k in fdic.keys():
                if k == good_name:
                    print("{},{:.2f}".format(k, eval(fdic[k][2])))
                    find_goods(fdic)
                    return 0
            print("商品库中无该商品")


def count(fdic, fn):
    type_amount = len(fdic)
    good_amount, total_sales, sum_price, ave_price = 0, 0, 0, 0
    for v in fdic.values():
        good_amount += eval(v[2])
        total_sales += eval(v[2]) * eval(v[1])
        sum_price += eval(v[1])
    try:
        ave_price = sum_price / type_amount
        with open(fn, "w") as f:
            text = "商品种类： " + str(type_amount) + \
                   "\n商品总数： " + str(good_amount) + \
                   "\n销售总额： " + str(total_sales) + \
                   "\n商品均价： " + str(ave_price)
            f.write(text)
    except ZeroDivisionError:
        with open(fn, "w+") as f:
            f.seek(0)
            text = "商品种类： 0\n商品总数： 0 \n销售总额： 0\n商品均价： 0"
            f.write(text)

    return print("商品统计数据已写入统计文件")


def main():
    goodinfo = "C:\\Users\\13935\\Desktop\\goodinformation.txt"  # 换成自己的路径
    goodtotal = "C:\\Users\\13935\\Desktop\\goodtotle.txt"  # 换成自己的路径
    goods_dict = read_goods(goodinfo)
    print("1. 查询商品\n2. 添加商品\n3. 统计商品\n4. 退出\n")
    while True:
        try:
            info = eval(input('请输入您的选择：'))
            if info == 1:
                find_goods(goods_dict)
            elif info == 2:
                add_goods(goods_dict, goodinfo)
            elif info == 3:
                count(goods_dict, goodtotal)
            elif info == 4:
                break
            else:
                print("输入错误请重新输入")
        except NameError:
            print("输入错误请重新输入")
    return 0


main()
