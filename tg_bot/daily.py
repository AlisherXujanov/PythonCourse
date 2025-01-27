import os
import requests
from env import RANDOM_IMG_URL
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
KEY = os.getenv("MY_TG_BOT")


async def start(update: Update, context: ContextTypes) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Google", callback_data="3",
                              url="https://www.google.com")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.edit_message_text(text=f"Selected option: {query.data}")

    if query.data == "1":
        await query.edit_message_text(text="You pressed button 1")

    elif query.data == "2":
        await query.edit_message_text(text='You pressed button 2')
        # End the query

    return await query.answer(text="You pressed Nothing!!!")


async def block_button(update: Update, context: ContextTypes) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [KeyboardButton("Hello World"), KeyboardButton("Option 2")],
        [KeyboardButton("Option 3")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def handle_responses(update: Update, context: ContextTypes) -> str:
    text: str = update.message.text.lower()
    username = update.message.from_user.username
    print(f"User {username} sent: {text}")
    response = ""

    if 'hello' in text:
        # \n  ->  is a new line
        response = f"Hello there {username}! How can i help you? \n"
    elif "how are you" in text:
        response = response + "I'm fine, thank you. And you? \n"
    elif 'show image' in text:
        with open("me.jpg", "rb") as f:
            """
                update.message.reply_photo(photo, caption=None)
                    photo   - Photo to send
                    caption - Photo caption, 0-1024 characters
            """
            await update.message.reply_photo(f, caption="Hello world! This is me!")
    elif 'send me mp3' in text:
        with open("music.mp3", "rb") as f:
            await update.message.reply_audio(f, caption="Hello world! This is me!")
    elif 'random image' in text:
        response = requests.get(RANDOM_IMG_URL)
        img = response.content
        await update.message.reply_photo(img, caption="Random image")
    elif 'block button' in text:
        await block_button(update, context)

    await update.message.reply_text(response)



if __name__ == "__main__":
    # Here we created our bot
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    app.add_handler(CommandHandler("start", start))

    # Inline button
    app.add_handler(CallbackQueryHandler(inline_button_handler))

    app.add_handler(CommandHandler("btn", block_button))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))

    app.run_polling(poll_interval=1)


# After creating a bot, we cann call some methods on it:
# RU: После создания бота, мы можем вызывать некоторые методы на нем:
# ====================================================================================================
# ADD HANDLER:

# - app.add_handler(handler)  -> Add a handler to the bot.
#                                A handler is a function that will be called when a specific event occurs.
#                                For example, when a user sends a message, the bot will call the handler
#                                that is responsible for handling messages.
#                                ----------------------------------------------
#                                RU: Добавить обработчик в бота.
#                                    Обработчик - это функция, которая будет вызываться, когда происходит
#                                    определенное событие. Например, когда пользователь отправляет сообщение,
#                                    бот вызовет обработчик, который отвечает за обработку сообщений.

# HANDLER TYPES:
# - CommandHandler  -> This handler is called when a user sends a command to the bot.
#                      RU: Этот обработчик вызывается, когда пользователь отправляет команду боту.
#                      ex:    /start, /help ...

# - MessageHandler  -> This handler is called when a user sends a message to the bot.
#                      RU: Этот обработчик вызывается, когда пользователь отправляет сообщение боту.
#                      ex:    "Hello", "How are you?" ...

# - CallbackQueryHandler  -> This handler is called when a user clicks on an inline button.
#                            ex:    InlineKeyboardButton("Option 1", callback_data="1") ...
# ====================================================================================================
# RUN POLLING:

# - app.run_polling(poll_interval=1)  -> Start the bot. This method will start the bot and will keep
#                                        it running until the user stops it. The poll_interval parameter
#                                        specifies how often the bot should check for new messages.
#                                        The default value is 1 second.
#                                        ----------------------------------------------
#                                        RU: Запустить бота.
#                                            Этот метод запустит бота и будет держать его запущенным,
#                                            пока пользователь не остановит его. Параметр poll_interval
#                                            указывает, как часто бот должен проверять новые сообщения.
#                                            Значение по умолчанию - 1 секунда.
# ====================================================================================================
# STOP:

# - app.stop()  -> Stop the bot. This method will stop the bot and will not allow it to receive any
#                  more messages. The bot can be started again by calling the run_polling method.
#                  This method is useful when you want to stop the bot temporarily, for example,
#                  when you are debugging the bot.
#                  ----------------------------------------------
#                  RU: Остановить бота.
#                      Этот метод остановит бота и не позволит ему получать больше сообщений.
#                      Бот может быть запущен снова, вызвав метод run_polling.
#                      Этот метод полезен,
#                      когда вы хотите временно остановить бота, например, когда вы отлаживаете бота.
# ====================================================================================================
