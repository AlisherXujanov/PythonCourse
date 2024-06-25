# Boolean  - True or False

# "", 0, False, None, [], {}, ()   -  NEGATIVES

# print(""    or "...")
# print(0     or "...")
# print(False or "...")
# print(None  or "...")

# print(10-10*1 or "...")

# print(bool(""))
# print(bool(0))
# print(bool(False))
# print(bool(None))

# def my_func(a, b):
#     return a + b

# x = my_func(4, -1)

# if x==1:
#     print("Positive 1")
# elif x==2:
#     print("Positive 2")
# elif x==3:
#     print("Positive 3")
# else:
#     print("Negative")


# def my_func(num):
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# def get_bigger(a, b):
#     if a > b:
#         print("A is bigger")
#     else:
#         print("B is bigger")

#         print("A is bigger")

# get_bigger(3+3, 5)

def get_biggest(a, b, c):
    if a > b and a > c:
        print("A is the biggest")
    elif b > a and b > c:
        print("B is the biggest")
    else:
        print("C is the biggest")


get_biggest(1, 2, 3)
get_biggest(333, 222, 111)
