"""Load Messages and log errors"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import external_functions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Enable logging
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):  #pylint: disable=unused-argument
    """Reply /start is issued."""
    update.message.reply_text('Hi! Send /help to learn more.')

def help(update, context):  #pylint: disable=unused-argument
    #pylint: disable=redefined-builtin
    """Send a message when the command /help is issued."""
    update.message.reply_text(external_functions.manual.main(update.message.text))

def user_stats(update, context):  #pylint: disable=unused-argument
    #pylint: disable=redefined-builtin
    """Send a message when the command /user_stats is issued."""
    update.message.reply_text(external_functions.user_stats.main(update.message.text))

def echo(update, context):  #pylint: disable=unused-argument
    """Echo the user message."""
    update.message.reply_text("Unrecognized command.")

def whoami(update, context):  #pylint: disable=unused-argument
    """Echo user information"""
    user_info = update.message.from_user
    echo_dname = f"Hello, {user_info['first_name']} {user_info['last_name']}\n\n"
    echo_uname = f"Username: {user_info['username']}\n"
    echo_langue = f"Display language: {user_info['language_code']}\n"
    echo_uid = f"User ID: {user_info['id']}\n"
    echo_result = (echo_dname + echo_uname + echo_langue + echo_uid)
    update.message.reply_text(echo_result)

def error(update, context):  #pylint: disable=unused-argument
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def ping(update, context):  #pylint: disable=unused-argument
    """Reply Pong if Ping is sent"""
    update.message.reply_text('Pong!')

def blocked(update, context):  #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.blocked_domains.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_blocked.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_blocked.txt", 'rb'))

def suspended(update, context):  #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.suspended_domains.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_suspended.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_suspended.txt", 'rb'))

def specs(update, context):  #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.specs.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_about.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_about.txt", 'rb'))

def statistics(update, context):  #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.statistics.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_stats.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_stats.txt", 'rb'))

def admin(update, context):  #pylint: disable=unused-argument
    """List admins on that target instance."""
    response_text = external_functions.admin.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_admin.txt", "w", encoding='utf-8') as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_admin.txt", 'rb'))

def trending_users(update, context):  #pylint: disable=unused-argument
    """List admins on that target instance."""
    response_text = external_functions.top_user.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_trendings.txt", "w", encoding='utf-8') as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_trendings.txt", 'rb'))

def main():
    """Start the bot."""
    updater = Updater(external_functions.utils.tokenization(), use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start)) #Command handler
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("ping", ping))
    updater.dispatcher.add_handler(CommandHandler("blocked_by", blocked))
    updater.dispatcher.add_handler(CommandHandler("specs", specs))
    updater.dispatcher.add_handler(CommandHandler("stats", statistics))
    updater.dispatcher.add_handler(CommandHandler("whoami", whoami))
    updater.dispatcher.add_handler(CommandHandler("trending_users", trending_users))
    updater.dispatcher.add_handler(CommandHandler("suspended_by", suspended))
    updater.dispatcher.add_handler(CommandHandler("user_stats", user_stats))
    updater.dispatcher.add_handler(CommandHandler("admins_on", admin)) #Command handler

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo)) #Echo unprocessable msgs
    updater.dispatcher.add_error_handler(error) # log all errors
    updater.start_polling() # Start the Bot
    updater.idle()

if __name__ == '__main__':
    main()
