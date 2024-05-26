# pipenv install python-telegram-bot
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
import logging
from openai import AsyncOpenAI
from env import OPEN_AI_KEY, KEY, RANDOM_IMG_URL

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=OPEN_AI_KEY,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1",
                                 url="https://t.me/+105hRD3w-xY2OTgy"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def block_button(update: Update, context: ContextTypes) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [KeyboardButton("Hello World"), KeyboardButton("Option 2")],
        [KeyboardButton("Option 3")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

    if query.data == "1":
        await query.edit_message_text(text="You pressed button 1")

    elif query.data == "2":
        await query.edit_message_text(text="You pressed button 2")
    elif query.data == "3":
        await query.edit_message_text(text="You pressed button 3")
    elif query.data == "4":
        await query.edit_message_text(text="You pressed button 4")
        # End the query
        return await query.answer(text="You pressed button 4")

    # If we want to answer the button by using another button we can use this:
    return await query.edit_message_text(
        text=f"Selected option: {query.data}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Answer", callback_data="4")]])
    )


async def help(update: Update, context: ContextTypes) -> None:
    return await update.message.reply_text("""
/help - Show this message
/start - Start the bot
""")


async def generate_response(message: str):
    chat_completion = await client.create_chat_completion(
        model="davinci",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )
    return chat_completion.choices[0].message.content


# Response
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

    elif 'block button' in text:
        await block_button(update, context)
    else:
        response = generate_response(text)

    await update.message.reply_text(response)


async def main():
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    # # Inline button
    app.add_handler(CallbackQueryHandler(inline_button_handler))
    # # Block button
    app.add_handler(CommandHandler("bbutton", block_button))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))

    # Run the bot
    print("Polling...")
    app.run_polling(poll_interval=1)


# Run the bot
if __name__ == "__main__":
    main()
