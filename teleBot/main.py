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
    update.message.reply_text("Hello there! I'm bot. Nice to see you!")


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
