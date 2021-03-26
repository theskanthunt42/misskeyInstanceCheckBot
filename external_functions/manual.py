"Placeholder"
def main(command_string):
    "Used as 'help' or 'man' just like linux"
    try:
        appendix = command_string.split(' ')[-1]
        if appendix == "/help":
            return(
                "Command Index:\n\n"
                "/help - Command Manual\n"
                "/stats - Show targeted instance statistics\n"
                "/whoami - Show your account infos\n"
                "/ping - Pong!\n"
                "/specs - Show targeted instance hardware specfications\n"
                "/blocked_by - Show domains blocked by targeted instance\n"
                "/suspended_by - Show domains suspended by targeted instance\n"
                "/admins_on - Show who is the admin on targeted instance\n"
                "/trending_users - Show most followed user on targeted instance\n"
                "/help - Show help menu or help for specific commands\n\n"
                "Syntax: {/command} {example_instance.com}\n"
                "Example #1: /specs rosehip.moe\n"
                "Example #2: /help help\n"
                )
        elif appendix == "start":
            return("Help message: /start\n"
            "How to use: /start\n"
            "Argument: None\n"
            "Infomation: Just a start command u will never use more than once"
            )
        elif appendix == "help":
            command_list = ['start', 'help', 'ping', 'blocked_by', 'specs',
            'stats', 'whoami', 'trending_users', 'suspended_by', 'admins_on']
            return(
            "Help message: /help\n"
            "How to use: /help [argument]\n"
            f"Argument: {command_list}\n"
            "Infomation: The help command now you are using now.\n"
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
            "Infomation: Show instances blocked by the target Misskey instance\n"
            )
        elif appendix == "specs":
            return(
            "Help message: /specs\n"
            "How to use: /specs [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show given instance's specfications.\n"
            )
        elif appendix == "stats":
            return(
            "Help message: /stats"
            "How to use: /stats [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show given instance's status.\n"
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
            "How to use: /trending_users [argument]"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: Show Trending Users from target instance.\n"
            )
        elif appendix == "suspended_by":
            return(
            "Help message: /suspended_by\n"
            "How to use: /suspended_by [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: List all instaces that blocked by given instance.\n"
            )
        elif appendix == "admins_on":
            return(
            "Help message: /admins_on\n"
            "How to use: /admins_on [argument]\n"
            "Argument: URL of a Misskey instance like https://misskey.io\n"
            "Infomation: List all admins from given instance.\n"
            )
        else:
            return "You've lost in the middle of nowhere. Did you mispelled something?"
    except Exception as warning_feedback:   #pylint: disable=broad-except:
        return warning_feedback
