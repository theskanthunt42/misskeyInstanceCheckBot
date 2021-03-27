"""To parse json from API"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """To return Top Users as str"""
    if len(command_string) <= 14:
        reply_text = 'Invaild instance url!'
    else:
        try:
            instance_url = command_string.split(' ')[-1].split('//')[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(instance_availability)
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/users/"
                api_payload = '{"limit":5, "sort":"+follower"}'
                api_result = requests.post(api_target, data=api_payload).json()
                expected_reply = ""
                expected_title = f"Top 5 users from {instance_url} (Sorted by followers):\n"
                expected_lnbreak = " \n"
                print(api_result)
                for i in api_result:
                    expected_name = f"Name: {i['name']}\n"
                    expected_username = f"Username: {i['username']}\n"
                    expected_id = f"ID: {i['id']}\n"
                    expected_description = f"Description: {i['description']}\n"
                    expected_foers = f"Followers: {i['followersCount']}\n"
                    expected_following = f"Following: {i['followingCount']}\n"
                    expected_note_counts = f"Notes count: {i['notesCount']}\n"
                    expected_admin_stats = f"Is a admin?: {i['isAdmin']}\n"
                    expected_bot_stats = f"Is a bot?: {i['isBot']}\n"
                    expected_last_active = f"Last activity: {i['updatedAt']}\n"
                    expected_reply += ("======================\n"
                                       + expected_name
                                       + expected_username
                                       + expected_id
                                       + expected_description
                                       + expected_foers
                                       + expected_following
                                       + expected_note_counts
                                       + expected_admin_stats
                                       + expected_bot_stats
                                       + expected_last_active
                                       + expected_lnbreak
                    )
                reply_text = expected_title + expected_lnbreak + expected_reply + expected_lnbreak
            else:
                reply_text = 'Instance unavailable!'
        except Exception as warning_feedback:  #pylint: disable=broad-except
            print(warning_feedback)
            reply_text = 'Instance unavailable!'
    return reply_text
