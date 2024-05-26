# https://github.com/openai/openai-python/blob/main/api.md

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
)
from requests import get
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from openai import AsyncOpenAI
from env import OPEN_AI_KEY, KEY, RANDOM_IMG_URL


# pipenv install openai
client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=OPEN_AI_KEY,
)


async def generate_response(message: str):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Hello! I am your AI assistant. How can I assist you today?')


async def block_button(update, context) -> None:
    keyboard = [
        [
            KeyboardButton("Random image"),
            KeyboardButton("Local image")
        ],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)



counter = 0
async def send_random_image(update, context) -> None:
    global counter
    counter += 1
    response = get(RANDOM_IMG_URL)
    file = response.content
    await update.message.reply_photo(photo=file, caption=f'Random image {counter}')


async def send_local_image(update, message) -> None:
    file = None
    with open('me.jpg', 'rb') as f:
        file = f.read()
        f.close()
    await update.message.reply_photo(photo=file)


async def respond(update: Update, context: CallbackContext) -> None:
    message = update.message.text.lower()
    client_username = update.message.from_user.username
    print(f"User {client_username} sent: {message}")
    response = "..."
    # -------------------------------------------------------------
    if 'random image' in message:
        await send_random_image(update, context)
    elif 'local image' in message:
        await send_local_image(update, context)
    else:
        response = await generate_response(message)
    await update.message.reply_text(response)


async def get_music(update, context):
    mp3 = ''
    with open('music.mp3', 'rb') as f:
        mp3 = f.read()
        f.close()
    await update.message.reply_audio(audio=mp3)



async def help(update, context) -> None:
    commands = """
Available commands:
/start
/help
/images
/music
"""
    await update.message.reply_text(commands)


# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    # Commands
    app.add_handler(CommandHandler("images", block_button))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("music", get_music))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, respond))

    # Run the bot
    print("Polling...")
    app.run_polling(poll_interval=1)
