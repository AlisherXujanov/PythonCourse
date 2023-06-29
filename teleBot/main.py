# pip install python-telegram-bot==13.7
import telegram.ext as tg_ext

TOKEN = "6069762613:AAEf6C36OQl7j8-HqKmCt-FQdcyUT6P7l2s"

print("Running up the bot...")

updater = tg_ext.Updater(TOKEN, use_context=True)
# This command is used to register the commands
# that the bot will be able to recognize and execute.
# use_context=True is used to tell the bot to use the new context based callbacks
# instead of the old deprecated ones.

dispatcher = updater.dispatcher


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
    with open("me.jpg", "rb") as f:
        """
                update.message.reply_photo(photo, caption=None)
            photo   - Photo to send
            caption - Photo caption, 0-1024 characters after entities parsing
        """
        update.message.reply_photo(f, caption="Hello world! This is me!")


def help(update, context):
    update.message.reply_text(
        """
        /start   - Start the bot
        /help    - Help
        /content - Get content
        """
    )


def content(update, context):
    update.message.reply_text("This is a custom command!")


dispatcher.add_handler(tg_ext.CommandHandler("start", start))
dispatcher.add_handler(tg_ext.CommandHandler("help", help))
dispatcher.add_handler(tg_ext.CommandHandler("content", content))

updater.start_polling()
updater.idle()
