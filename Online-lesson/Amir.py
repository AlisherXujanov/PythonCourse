
def get_max(a,b,c) -> int:
    return a if a > b and a > c else (b if b > c and b > a else c)


a = 1
b = 2
c = 3
r = get_max(a,b,c)
print(r)
 
text = "Hello, this is 3rd task 9 1 2"
result = [num for num in text if num.isnumeric()]
