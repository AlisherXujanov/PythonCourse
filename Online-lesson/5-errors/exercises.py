# 1. Напишите логику, которая проверяет, является ли число положительным, 
# отрицательным или нулем. 

num = 15
r = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
print(r)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Напишите логику, которая проверяет, четное число или нет. 
"Done"

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Напишите логику, которая проверяет, кратно ли число на 3 и 5 одновременно.
# (делится ли число и на 3 и на 5 одновременно без остатка)
r = "Yes" if num % 3 == 0 and num % 5 == 0 else "No"
print(r)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Напишите логику, которая проверяет, пустая строка или нет
txt = ""
r = "Yes" if len(txt)==0 else "No"
print(r)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Напишите логику, которая проверяет, содержит ли строка определенный символ. 
txt = "Hello $"
symbol = "$"
r = "Yes" if symbol in txt else "No"
print(r)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Напишите логику, которая проверяет, начинается ли строка с определённого символа. 
txt = "Hello $"
symbol = "$"
r = "Yes" if txt.startswith(symbol) else "No"
print(r)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


