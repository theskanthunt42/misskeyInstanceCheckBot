"""Contains function for top_user.py"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """Return Admins on any specified Misskey instance in a formatted way as str"""
    try:
        instance_url = command_string.split(' ')[-1].split('//')[-1]
        api_result = \
            requests.post(f"https://{instance_url}/api/users/", data='{"limit":100, "state":"admin"}').json()
        expected_reply = ""
        for items in api_result:
            expected_reply += (f"Name: {items['name']}\n"
                                f"Username: {items['username']}\n"
                                f"ID: {items['id']}\n"
                                f"Created at {items['createdAt']}\n"
                                f"Last activity: {items['updatedAt']}\n"
                                f"Description: {items['description']}\n"
                                f"Birthday: {items['birthday']}\n"
                                f"Location: {items['location']}\n"
                                f"Following: {items['followingCount']}\n"
                                f"Followers: {items['followersCount']}\n"
                                f"Total notes: {items['notesCount']}\n"
                                f"Two Factor Enable: {items['twoFactorEnabled']}\n"
                                f"Enable password-less login?: {items['usePasswordLessLogin']}\n\n"
            )
        return f"Admins on {instance_url}:\n\n" + expected_reply

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

print(Main("/admins_on rosehip.moe"))