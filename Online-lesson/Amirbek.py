# Напишите логику, которая находит самую короткую строку в массиве строк
def get_small_word(text:str) -> str:
    memory = text.split(" ")[0]
    for word in text.split(" "):
        if len(word) < len(memory): 
            memory = word
    return memory 

res = get_small_word("Hello, world my name is Amirbek") 
print(res)