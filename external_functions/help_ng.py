"""Help command stuff String that should come in: /help {command}"""
def main(command_string):
    command_split = command_string.split(' ')
    command_list = ['start', 'help', 'ping', 'blocked_by', 'specs', 'stats', 'whoami', 'trending_users', 'suspended_by', 'admins_on']
    if len(command_split) != 2:
        reply_text = 'Use /help {command} to get help infomations!'
    else:
        if command_split[1] not in command_list:
            reply_text = 'Please give a correct argument\nLike: /help help'
        else:
            if command_split[1] is command_list[0]:
                reply_text = """
                Help message: /start
                How to use: /start
                Argument: None
                Infomation: Just a start command u will never use more than once
                """
            elif command_split[1] is command_list[1]:
                reply_text = f"""
                Help message: /help
                How to use: /help [argument]
                Argument: {command_list}
                Infomation: The help command now you are using now.
                """
            elif command_split[1] is command_list[2]:
                reply_text = """
                Help message: /ping
                How to use: /ping
                Argument: None
                Infomation: Pong!
                """
            elif command_split[1] is command_list[3]:
                reply_text = """
                Help message: /blocked_by
                How to use: /blocked_by [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: Show instances blocked by the target Misskey instance
                """
            elif command_split[1] is command_list[4]:
                reply_text = """
                Help message: /specs
                How to use: /specs [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: Show given instance's specfications.
                """
            elif command_split[1] is command_list[5]:
                reply_text = """
                Help message: /stats
                How to use: /stats [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: Show given instance's status.
                """
            elif command_split[1] is command_list[6]:
                reply_text = """
                Help message: /whoami
                How to use: /whoami
                Argument: None
                Infomation: Show who the fuck you are.
                """
            elif command_split[1] is command_list[7]:
                reply_text = """
                Help message: /trending_users
                How to use: /trending_users [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: Show Trending Users from target instance.
                """
            elif command_split[1] is command_list[8]:
                reply_text = """
                Help message: /suspended_by
                How to use: /suspended_by [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: List all instaces that blocked by given instance.
                """
            elif command_split[1] is command_list[9]:
                reply_text = """
                Help message: /admins_on
                How to use: /admins_on [argument]
                Argument: URL of a Misskey instance like https://misskey.io
                Infomation: List all admins from given instance.
                """
            else:
                reply_text = "Internal error!"
    return reply_text