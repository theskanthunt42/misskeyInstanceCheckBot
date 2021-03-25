import requests
#https://rosehip.moe/api-doc#operation/users/stats
#Command sting should be like:
#/user_stats [username] [api_host]
#username: sth like 
def main(command_string):
    splited_command = command_string.split(' ')
    