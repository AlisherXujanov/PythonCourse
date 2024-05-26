
# Introduction
1. From telegram BotFather you will get a token that you need to get started with the bot. 
<br>
-- RU: От BotFather вы получите токен, который вам нужно получить, чтобы начать работу с ботом.

<br>
2. Create a python file and write your token in it. 
<br>
-- RU: Создайте файл python и напишите в нем свой токен.

<br>
3. Install the python-telegram-bot library using pip install python-telegram-bot  
<br>
-- RU: Установите библиотеку python-telegram-bot, используя pip install python-telegram-bot

<br>

```bash
pip install python-telegram-bot
```
1. Create a bot instance using the token you got from the BotFather.
<br>
<br>
-- RU: Создайте экземпляр бота, используя токен, который вы получили от BotFather.


2. Create a function that will be called whenever a user sends a message to the bot.
<br>
<br>
-- RU: Создайте функцию, которая будет вызываться каждый раз, когда пользователь отправляет сообщение боту.

ex:  
```python
def start(update, context):
    context.bot.send_message("Hello World")
```


---
# Buttons
<!-- BUTTONS -->
The python-telegram-bot library supports two types of buttons: InlineKeyboardButton and KeyboardButton.
<br>
<br>
-- RU: Библиотека python-telegram-bot поддерживает два типа кнопок: InlineKeyboardButton и KeyboardButton.


- InlineKeyboardButton: These buttons are often used within a custom keyboard for inline queries. When the user clicks an inline button, Telegram clients will display a progress bar until you call answerCallbackQuery. Here's an example of how to use it:
<br>
<br>
-- RU: Эти кнопки часто используются внутри пользовательской клавиатуры для встроенных запросов. Когда пользователь нажимает на встроенную кнопку, клиенты Telegram отображают полосу прогресса до тех пор, пока вы не вызовете answerCallbackQuery. Вот пример использования:

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

- KeyboardButton: These buttons are part of a custom keyboard attached to the message. They are simpler than inline buttons. Here's an example of how to use it:
<br>
<br>
-- RU: Эти кнопки являются частью пользовательской клавиатуры, прикрепленной к сообщению. Они проще, чем встроенные кнопки. Вот пример использования:


```python
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler

def start(update, context):
    keyboard = [[KeyboardButton("Option 1"), KeyboardButton("Option 2")]]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

In both examples, when the /start command is sent, a message with a custom keyboard is sent. The user can then select an option from the keyboard.


# To create requirements.txt file
1. ```pipenv lock -r > requirements.txt```  - is outdated
2. 🎯 New version is: ```pipenv run pip freeze  > requirements.txt``` 