# pip install python-telegram-bot==13.7
from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "6069762613:AAEf6C36OQl7j8-HqKmCt-FQdcyUT6P7l2s"

RANDOM_IMAGE = "Random image"
GET_MP3 = "Get mp3"
RANDOM_IMG_URL = "https://picsum.photos/1200"

# Declare IMAGE_COUNTER as a global variable
global IMAGE_COUNTER
IMAGE_COUNTER = 0


print("Running up the bot...")

# This command is used to register the commands
# that the bot will be able to recognize and execute.
# use_context=True is used to tell the bot to use the new context based callbacks
# instead of the old deprecated ones.


def start(update, context):
    # SENDING HELLO MESSAGE
    # .reply_text(message, reply_markup=None, **kwargs)
    # update.message.reply_text("Hello there! I'm bot. Nice to see you!")
    # ###################################################################
    # SENDING PHOTO
    _send_local_file(update, context)


def _send_local_file(update, context):
    """
        We must open the file in binary mode, 
        otherwise Telegram will not be able to process it correctly
        ------------------------------------------------------------
        RU: Мы должны открыть файл в двоичном режиме,
        иначе Telegram не сможет обработать его правильно
    """
    with open("teleBot/me.jpg", "rb") as f:
        """
                update.message.reply_photo(photo, caption=None)
            photo   - Photo to send
            caption - Photo caption, 0-1024 characters
        """
        update.message.reply_photo(f, caption="Hello world! This is me!")


def get_buttons(update: Updater, context: CallbackContext):
    buttons = [
        [KeyboardButton(RANDOM_IMAGE)],
        [KeyboardButton(GET_MP3)]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose option:",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )


def message_handler(update: Updater, context: CallbackContext):
    # Use the global keyword to modify IMAGE_COUNTER
    global IMAGE_COUNTER
    IMAGE_COUNTER += 1
    if update.message.text == RANDOM_IMAGE:
        image = get(RANDOM_IMG_URL).content
        context.bot.sendMediaGroup(
            chat_id=update.effective_chat.id,
            media=[InputMediaPhoto(image, caption=f"Random {IMAGE_COUNTER}")]
        )
    elif update.message.text == GET_MP3:
        _send_mp3(update, context)


def help(update, context):
    update.message.reply_text("""/start   - Start the bot
                                /help    - Help
                                /content - Get content
                                /buttons
                                """
                              )


updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler('buttons', get_buttons))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))


updater.start_polling()
updater.idle()
