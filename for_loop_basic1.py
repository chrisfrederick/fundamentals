# for x in range(150):
#     print(x)

# for z in range(5, 1000, 5):
#     print(z)

# for a in range(1, 100):
#     if a%5 == 0:
#         a="Coding"
#         print(a)
#     elif a%10 == 0:
#         a="Coding Dojo"
#         print(a)
#     else:
#         print(a)


# sum =0
# for i in range(1, 500000 + 1, 2):
#     sum+=i
# print(sum)


# for i in range(2018, 0, -4):
#     print(i)


# low_num = 2
# high_num = 9
# mult = 3
# for i in range(low_num, high_num + 1):
#     if i % mult == 0:
#         print(i)


def multiply(num_list, num):
    for x in num_list:
        x *= num
    return x
a = [2,4,10,16]
b = multiply(a,5)
print(b)