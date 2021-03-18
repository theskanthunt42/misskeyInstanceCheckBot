"""Followers from target fediverse instance"""
"""command: /fedi_follow_by"""
def Main(command_string):
    if len(command_string) <= 17:
        reply_text = 'Invaild instance url!'
    else:
        