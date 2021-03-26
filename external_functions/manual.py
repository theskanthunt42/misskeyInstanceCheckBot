"Manual.py"
def main(command_string):
    "Used as 'help' or 'man' just like linux"
    try:
        appendix = command_string.split(' ')[-1]
        if appendix == "/help":
            return(
                "Command Index:\n\n"
                "/help - Show help menu or help for specific commands\n"
                "/stats - Show statistics of specified instance\n"
                "/whoami - Show your information\n"
                "/ping - Replies Pong\n"
                "/specs - Show hardware specs of specified instance\n"
                "/blocked_by - Show domains blocked by specified instance\n"
                "/suspended_by - Show domains suspended by specified instance\n"
                "/admins_on - Show admins of specified instance\n"
                "/trending_users - Show most followed user on targeted instance\n"
                "Syntax: {/command} {example_instance.com}\n\n"
                "Example #1: /specs rosehip.moe\n"
                "Example #2: /help help\n"
                )
        elif appendix == "start":
            return("Help message: /start\n"
            "How to use: /start\n"
            "Argument: None\n"
            "Infomation: Hi!\n"
            )
        elif appendix == "help":
            command_list = ['start', 'help', 'ping', 'blocked_by', 'specs',
            'stats', 'whoami', 'trending_users', 'suspended_by', 'admins_on']
            return(
            "Help message: /help\n"
            "How to use: /help [argument]\n"
            f"Argument: One of the commands from {[command_list]}\n"
            "Infomation: The help command that you are currently using.\n"
            )
        elif appendix == "ping":
            return(
            "Help message: /ping\n"
            "How to use: /ping\n"
            "Argument: None\n"
            "Infomation: Pong!\n"
            )
        elif appendix == "blocked_by":
            return(
            "Help message: /blocked_by\n"
            "How to use: /blocked_by [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show domains that are currently blocked by specified Misskey instance.\n"
            )
        elif appendix == "specs":
            return(
            "Help message: /specs\n"
            "How to use: /specs [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show given specifications by specified Misskey instance.\n"
            )
        elif appendix == "stats":
            return(
            "Help message: /stats\n"
            "How to use: /stats [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show given statistics by specified Misskey instance.\n"
            )
        elif appendix == "whoami":
            return(
            "Help message: /whoami\n"
            "How to use: /whoami\n"
            "Argument: None\n"
            "Infomation: Show who you are.\n"
            )
        elif appendix == "trending_users":
            return(
            "Help message: /trending_users\n"
            "How to use: /trending_users [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show trending users of specificed instance.\n"
            )
        elif appendix == "suspended_by":
            return(
            "Help message: /suspended_by\n"
            "How to use: /suspended_by [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: List Domains that are blocked by specified instance.\n"
            )
        elif appendix == "admins_on":
            return(
            "Help message: /admins_on\n"
            "How to use: /admins_on [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show Admins of specificed instance.\n"
            )
        else:
            return "You've lost in the middle of nowhere. Did you misspell anything?"
    except Exception as warning_feedback:   #pylint: disable=broad-except:
        return warning_feedback
