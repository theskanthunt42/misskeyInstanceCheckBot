"""Contains function for top_user.py"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """Return current trending users on any specified Misskey instance in a formatted way as str"""
    try:
        instance_url = command_string.split(' ')[-1].split('//')[-1]
        api_target = f"https://{instance_url}/api/users/"
        api_payload = '{"limit":5, "sort":"+follower"}'
        api_result = requests.post(api_target, data=api_payload).json()
        reply_text = ""
        for items in api_result:
            reply_text += ("======================\n\n"
                                f"Name: {items['name']}\n"
                                f"Username: {items['username']}\n"
                                f"ID: {items['id']}\n"
                                f"Description: {items['description']}\n"
                                f"Followers: {items['followersCount']}\n"
                                f"Following: {items['followingCount']}\n"
                                f"Notes count: {items['notesCount']}\n"
                                f"Is a admin?: {items['isAdmin']}\n"
                                f"Is a bot?: {items['isBot']}\n"
                                f"Last activity: {items['updatedAt']}\n"
            )
        return f"Top 5 users from {instance_url} (Sorted by followers):\n" + reply_text

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except
