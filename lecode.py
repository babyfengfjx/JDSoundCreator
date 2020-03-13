# from collections import Counter
#
# l = [2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1]
#
#
#
# a = dict(Counter(l))
# b = sorted(a, key=lambda x: a[x],reverse= True)
# print(a)
# print(b)
# if a[b[0]] >len(l)/2:
#     print(b[0])
# # for i in a:
# #     if a[i] > len(l) / 2:
# #         print(i)
# #


# x = -1230
# # x = str(x)
# # if '-' in x :
# #     out = '-' + x[1:][::-1]
# # else:
# #     out = x[::-1]
# # print( int(out))
n = 0b00000010100101000001111010011100


# n = int(n)
# # print(n)
n = str(bin(n))
print(n)
n = n[::-1][:-2]
print(type(n))
print(int(n,2))
print(n)
# print(bin(n))

# # print(bin(int(n[:-2:-1])))