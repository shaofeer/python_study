import random

# line = input("input :")
# input_list = line.split(",")
#
# temp = ['upp', 'wint']
# res1 = input_list * 3 + temp
# res2 = res1[:]
#
# print(res1)
# print(res2)
# print(res1 is res2)
#
# n = input("input n:")
#
# n = int(n)
#
# arr = []
# for i in range(0, n):
#     rn = random.randint(0, n)
#     arr.append(int(rn))
#
# print(arr)
#
# arr.clear()
#
# for i in range(0, n):
#     rn = random.randrange(start=1, stop=n, step=2)
#     arr.append(int(rn))
#
# print(arr)
#
# arr.clear()
#
# for i in range(0, n):
#     rn = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     arr.append(rn)
#
# print(arr)
#
#

#
# x = input("input N number:")
# print(x)
#
# llc = x.split(' ')
# ss = set(llc)
#
# print(ss)


# x = input("input N number:")
# print(x)
# list = x.split(' ')
#
# list = [x.__hash__() for x in list]
#
# aa = tuple(list)
#
# print(aa)


x = input("input N number:")

words = x.split(' ')

di = dict()

for word in words:
    count = 1
    if di.get(word) is not None:
        count += di.get(word)

    di[word] = count

print(di)
