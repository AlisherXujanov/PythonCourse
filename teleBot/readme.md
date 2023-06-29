1. From telegram BotFather you will get a token that you need to get started with the bot. 
2. Create a python file and write your token in it. 
3. Install the python-telegram-bot library using pip install python-telegram-bot
4. Create a bot instance using the token you got from the BotFather.
5. Create a function that will be called whenever a user sends a message to the bot.
   ex:  
    def start(update, context):
        context.bot.send_message("Hello World")

6. Instantiate an updater object with the token you got from the BotFather and create a dispatcher object from it.
7. Create a handler object for the command /start and pass the function start to it.
   ex: 
    dispatcher.add_handler(tg_ext.CommandHandler("start", start))
8. Start polling the bot to check for new messages.
    updater.start_polling()
    updater.idle()
9. Run the python file and start chatting with your bot.

