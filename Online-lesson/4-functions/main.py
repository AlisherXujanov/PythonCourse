# def - define

# def send_message(to_person):
#     print(f"Sending message to {to_person} ...")


# name = "Amir"
# send_message(name)


# name = "Amirbek"
# send_message(name)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# def plus(a, b, c, d, e):
#     return a + b + c + d + e


# res = plus(1, 2, 3, 4, 5, 6)
# print(res)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# def plus(*args):
#     # args == [..., ...]
#     return sum(args)

# res = plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(res)

# res = plus(*list(range(100)))
# print(res)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def get_bigger(num1:int, num2:int) -> int:
    if num1 > num2:
        return num1
    else:
        return num2


def get_biggest_of_three(n1:int, n2:int, n3:int) -> int:
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

get_biggest_of_three(1, 2, 3)   # 3
get_biggest_of_three(10, 5, 55) # 55
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# Напишите логику, которая находит самую длинную строку в тексте.


def get_longest_word(text:str) -> str:
    memory = ''
    # "Hello, my name is ..."  = ["Hello,", "my", "name", "is", ...]
    for word in text.split(" "):
        if len(word) > len(memory):
            memory = word
    return memory

res = get_longest_word("Hello, my name is Amirbek") # Amirbek
print(res)

res = get_longest_word("Hello, my name is Amir and I am a programmer") # programmer
print(res)


