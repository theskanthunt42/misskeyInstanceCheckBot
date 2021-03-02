"""Load Messages and log errors"""
import logging
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import external_functions.blocked_domains
import external_functions.specs
import external_functions.statistics
import external_functions.suspended_domains
import external_functions.admin

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Enable logging
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    #pylint: disable=unused-argument
    """Reply /start is issued."""
    update.message.reply_text('Hi! Send /help to learn more.')

def help(update, context):
    #pylint: disable=unused-argument
    """Send a message when the command /help is issued."""
    update.message.reply_text("Command Index:\n\n"
                                "/help - Command Manual\n"
                                "/stats - Show targeted instance statistics\n"
                                "/whoami - Show your account infos\n"
                                "/ping - Pong!\n"
                                "/specs - Show targeted instance hardware specfications\n"
                                "/blocked_by - Show domains blocked by targeted instance\n"
                                "/suspended_by - Show domains suspended by targeted instance\n"
                                "/admins_on - Show who is the admin on targeted instance\n"
                                " \n"
                                "Syntax: {/command} {example_instance.com}\n"
                                "Example: /specs rosehip.moe\n")

def echo(update, context):
    #pylint: disable=unused-argument
    """Echo the user message."""
    update.message.reply_text(f"{update.message.text} is not a recognized command.")

def whoami(update, context):
    #pylint: disable=unused-argument
    """Echo user information"""
    user_info = update.message.from_user
    echo_title = "Who are you:\n\n"
    if user_info['first_name'] == 'None':
        user_first_name = ' '
    else:
        user_first_name = user_info['first_name']
    if user_info['last_name'] == 'None':
        user_last_name = ' '
    else:
        user_last_name = user_info['last_name']
    echo_dname = f"Display name: {user_first_name} {user_last_name}\n"
    echo_uname = f"Username: {user_info['username']}\n"
    echo_langue = f"Display language: {user_info['language_code']}\n"
    echo_uid = f"UID: {user_info['id']}\n"
    echo_chatid = f"Chat ID: {update.message.chat_id}\n"
    echo_result = (echo_title + echo_dname + echo_uname + echo_langue + echo_uid + echo_chatid)
    update.message.reply_text(echo_result)

def error(update, context):
    #pylint: disable=unused-argument
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def ping(update, context):
    #pylint: disable=unused-argument
    """Reply Pong if Ping is sent"""
    update.message.reply_text('Pong!')

def blocked(update, context):
    #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.blocked_domains.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_blocked.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_blocked.txt", 'rb'))

def suspended(update, context):
    #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.suspended_domains.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_suspended.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_suspended.txt", 'rb'))

def specs(update, context):
    #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.specs.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_about.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_about.txt", 'rb'))

def statistics(update, context):
    #pylint: disable=unused-argument
    """List domains blocked by targeted instance."""
    response_text = external_functions.statistics.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_stats.txt", "w", encoding="utf-8") as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_stats.txt", 'rb'))

def admin(update, context):
    #pylint: disable=unused-argument
    """List admins on that target instance."""
    response_text = external_functions.admin.Main(update.message.text)
    if len(response_text) <= 4096:
        update.message.reply_text(response_text)
    else:
        with open("cache_admin.txt", "w", encoding='utf-8') as text_file:
            text_file.write(response_text)
        update.message.reply_document(open("cache_admin.txt", 'rb'))

def tokenization():
    """Read token from specified location."""
    with open('config.json', 'r') as token_container:
        token_variable = json.loads(token_container.read())
        key = token_variable['token']
        return key

def main():
    """Start the bot."""
    updater = Updater(tokenization(), use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start)) #Command handler
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("ping", ping))
    updater.dispatcher.add_handler(CommandHandler("blocked_by", blocked))
    updater.dispatcher.add_handler(CommandHandler("specs", specs))
    updater.dispatcher.add_handler(CommandHandler("stats", statistics))
    updater.dispatcher.add_handler(CommandHandler("whoami", whoami))
    updater.dispatcher.add_handler(CommandHandler("suspended_by", suspended)) #Command handler
    updater.dispatcher.add_handler(CommandHandler("admins_on", admin))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo)) #Echo unprocessable msgs
    updater.dispatcher.add_error_handler(error) # log all errors
    updater.start_polling() # Start the Bot
    updater.idle()

if __name__ == '__main__':
    main()
