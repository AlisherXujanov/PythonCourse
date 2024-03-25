# 1. Open the script ordering_system.py present inside the project folder.
# RU: Откройте скрипт этот_файл.py, находящийся внутри папки проекта.
# =============================================================================
# 2. Run the script and, when requested, enter in the three products of your 
# choice based on the menu - 1 = espresso, 2 = coffee etc.
# RU: Запустите скрипт и, когда потребуется, введите три продукта на ваш выбор
# на основе меню - 1 = эспрессо, 2 = кофе и т.д.
# =============================================================================
# 3. To run the script, open terminal and execute the following command.
# •	python3 этот_файл.py
# RU: Чтобы запустить скрипт, откройте терминал и выполните следующую команду.
# •	python3 этот_файл.py
# =============================================================================
# 4. Extend the script to have a new function called calculate_subtotal.
# It should accept one argument which is the order list and return the sum
# of the prices of the items in the order list.
# RU: Расширьте скрипт, чтобы добавить новую функцию с именем calculate_subtotal.
# Он должен принимать один аргумент - список заказов и возвращать сумму цен товаров в списке заказов.
# =============================================================================
# 5. Implement calculate_tax() which calculates the tax of the subtotal.
# The tax percentage is 15% of overall bill.
# RU: Реализуйте calculate_tax (), который рассчитывает налог с промежуточного итога.
# Процент налога составляет 15% от общего счета.
# =============================================================================
# 6. Implement summarize_order() which returns a list of the names of the items
# that the customer ordered and the total amount (including tax) that they have to pay.
# The orders should show the name and price.
# RU: Реализуйте summarize_order (), который возвращает список имен товаров,
# которые заказал клиент, и общую сумму (включая налог), которую он должен заплатить.
# Заказы должны показывать название и цену.

menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee',   "price": 2.50},
    3: {"name": 'cake',     "price": 2.79},
    4: {"name": 'soup',     "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order):
    """ 
        Calculates the subtotal of an order
        RU: Рассчитывает промежуточный итог заказа

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum
        RU: Сложите цены всех товаров в заказе и верните сумму

    Args:
        order: list of dicts that contain an item name and price
        RU: список словарей, содержащих имя и цену товара

    Returns:
        float = The sum of the prices of the items in the order
        RU: Сумма цен товаров в заказе
    """

    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    ### НАПИШИТЕ СВОЕ РЕШЕНИЕ ЗДЕСЬ

    raise NotImplementedError()
    ### DELETE ERROR AFTER IMPLEMENTATION OF SOLUTION
    ### УДАЛИТЕ СТРОКУ С ОШИБКОЙ ПОСЛЕ РЕАЛИЗАЦИИ РЕШЕНИЯ

def calculate_tax(subtotal):
    """ 
        Calculates the tax of an order
        RU: Рассчитывает налог заказа

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.
        RU: Умножьте промежуточный итог на 15% и верните произведение, округленное до двух десятичных знаков.

    Args:
        subtotal: the price to get the tax of
        RU: цена для получения налога

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
        RU: Налог, необходимый для заданного промежуточного итога, который составляет 15% и округляется до двух десятичных знаков.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE

    raise NotImplementedError()

def summarize_order(order):
    """ Summarizes the order
        RU: Резюмирует заказ

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.
        
        RU: 
        1. Рассчитайте итоговую сумму (промежуточный итог + налог) и сохраните ее в переменной с именем total (округлено до двух десятичных знаков)
        2. Сохраните только имена всех товаров в заказе в списке с именем names
        3. Верните имена и итоговую сумму.

    Args:
        order: list of dicts that contain an item name and price
        RU: список словарей, содержащих имя и цену товара

    Returns:
        tuple of names and total. The return statement should look like 
        RU: кортеж имен и итоговой суммы. Оператор return должен выглядеть как
        
        return names, total
        RU: return names, total
    """
    print_order(order)
    ### WRITE SOLUTION HERE

    raise NotImplementedError()


# This function is provided for you, and will print out the items in an order
# RU: Эта функция предоставляется вам и будет печатать товары в заказе
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    # RU: Вы заказали ' + str(len(order)) + ' товаров')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


# This function is provided for you, and will display the menu
# RU: Эта функция предоставляется вам и будет отображать меню
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
# RU: Эта функция предоставляется вам и будет создавать заказ, предлагая пользователю выбрать товары из меню
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        # RU: Выберите номер товара в меню ' + str(count) + ' (от 1 до 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.

RU: Вот несколько примеров вызовов функций, которые помогут вам протестировать свои реализации.
Не стесняйтесь изменять, раскомментировать и добавлять их по своему усмотрению.
'''
def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)



