# Напишите логику, которая находит самую короткую строку в массиве строк
def get_shortest_word(text:str) -> str:
    memory = text.split(" ")[0]
    for word in text.split(" "):
        if len(word) < len(memory): 
            memory = word
    return memory 

res = get_shortest_word("Hello, my name is Amirbek") # Amirbek
print(res)

res = get_shortest_word("Hello, my name is Amir and I am a programmer") # programmer
print(res)

