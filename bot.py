from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scraper import scrape_movie


bot_token = "YOUR_BOT_TOKEN"

keys = ["title", "rating", "duration"]


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi! I can help you search movies on IMDB.\nPlease enter /movie to get started")


def movie(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please enter the name of the movie you wish to search for!")


def search_movie(update, context):
    movie_name = update.message.text
    update.message.reply_text("Searching for details of "+movie_name)
    print(movie_name)
    movie_info = scrape_movie(movie_name=movie_name)
    for key in keys:
        update.message.reply_text(
            "The "+key+" of the movie is "+movie_info[key])
    update.message.reply_text("There you go!")


def run_bot():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    # Add command handler
    start_command_handler = CommandHandler('start', start)
    movie_command_handler = CommandHandler('movie', movie)
    # Add message handler
    movie_handler = MessageHandler(Filters.text, search_movie)
    dp.add_handler(start_command_handler)
    dp.add_handler(movie_command_handler)
    dp.add_handler(movie_handler)
    updater.start_polling()
    updater.idle()


run_bot()
