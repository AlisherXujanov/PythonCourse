# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for letter in l:
#     print(letter.upper())
# ---------------------------------------------------------------------
words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry',
              'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

result = ""
for word in words_list:
    if len(word) > len(result):
        result = word
print(result)
# ---------------------------------------------------------------------
