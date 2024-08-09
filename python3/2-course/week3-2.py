# Question: 1
# Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.
# Solution:

olympics = 'Beijing', 'London', 'Rio', 'Tokyo'
print(olympics) 
# =================================================================================
# =================================================================================
# Question: 2
# The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable
# country.
# Solution:

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012),
              ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for pair in tuples_lst:
    country.append(pair[1])
print(country) 
# =================================================================================
# =================================================================================
# Question: 3
# With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.
# Solution:

olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp
# =================================================================================
# =================================================================================
# Question: 4
# Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple
# with all five parameters in that order.
# Solution:
def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown
# =================================================================================
# =================================================================================
# Question: 5
# Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics.
# Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items()
# method provides a list of tuples. Do not use .keys() method.
# Solution:
gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13,
        'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}
num_medals = []
for pair in gold.items():
    num_medals.append(pair[1])
print(num_medals) 