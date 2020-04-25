def str_bin():
    """
    将二进制字符串转换成二进制数的过程
    Returns
    -------

    """
    s = '0b10001001010101'
    print(int(s,2))
    print(bin(int(s,2)))

import re
def str_find():
    """
    给定一个长字符串A，一个子字符串B；
    查找出B在A中出现的次数，并返回B所在A中的位置
    Returns
    -------

    """
    s = 'babyfengbabyzhopanbabyfengxintongbabyfast'
    sub = 'baby'
    for i in  re.finditer(sub,s):
        print(i.start())#获取开始的位置信息
        print(i.group(),i.span())#获取具体找到的文本和起开始以及结束位置信息


# str_find()
def continue_sum ():
    """
    给定一个正整数，判断这个正整数是否可以分解成连续正整数的和，如果可以分解就打印出所有情况的值，如果不能就输出NONE.

    -------

    """

    while True:
        try:
            n = int(input("请输入一个正整数： "))  #记得input输入的任何内容都是字符串，需要转成整型
            flag = 0  # 设置标志位，只要有一个满足要求的输出就转换标志，如果一个都没有那么就可以输出NONE
            for m in range(2,int(n/2)+2): #这里的m就是代表有多少个连续的数，其实m的范围不会超过这个整数的一半，这里+2是因为在数字3的时候发现的
                num =(2*n+m-m**2)%(2*m) #num就是为了判断能够被整除了。
                num_1 = int((2*n+m-m**2)/(2*m)) #这个num_1 其实就是第一个起始数字，那么num_1肯定是一个大于1的正整数，这个算式就是采用了这个规律，使用首数加尾数乘以个数除以2得到的。
                if num == 0 and num_1 >= 1: #如果能被整除，说明这个数是一个正整数，如果大于等于1那么就是满足要求的，因为有可能为0；
                    list_out = [x+num_1 for x in range(m)] #这里就是生成实际可行的数列了
                    print(list_out)
                    flag =1 #一旦有可能的方案，就转换标志位
            if flag == 0:
                print("NONE")
        except:
            break
continue_sum()
