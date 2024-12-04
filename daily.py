

def get_input_and_count_vowels():
    vowels = 'aioue'
    answer = input("Write something: ")
    for l in answer:
        if l.isalpha():
            l = l.lower()
            if l in vowels:
                ...  # vowels_count += 1
            else:
                ...  # constants_count += 1
    return f"Vowels: {vowels_count} and constants: {constants_count}"