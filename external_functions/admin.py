"""To lookup admins of a specific instance"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """Look up who is the admin on that instance"""
    if len(command_string) <= 11:
        reply_text = 'Invaild instance url!'
    else:
        try:
            instance_url = \
                command_string.split(' ')[-1].split('//')[-1].split('/')[0]
            instance_availability = requests.get(
                f'https://{instance_url}').status_code
            print(f'{instance_availability} {instance_url}')
            if instance_availability == 200:
                api_target = f'https://{instance_url}/api/users/'
                api_payload = '{"limit":100, "state":"admin"}'
                api_result = requests.post(api_target, data=api_payload).json()
                expected_reply = ''
                expected_title = f'Admins on {instance_url}:\n'
                expected_lnbreak = '\n'
                for i in api_result:
                    expected_name = f"Name: {i['name']}\n"
                    expected_username = f"Username: {i['username']}\n"
                    expected_user_id = f"ID: {i['id']}\n"
                    expected_create_time = f"Created at {i['createdAt']}\n"
                    expected_last_update = f"Last activity: {i['updatedAt']}\n"
                    expected_description = f"Description: {i['description']}\n"
                    expected_birthday = f"Birthday: {i['birthday']}\n"
                    expected_location = f"Location: {i['location']}\n"
                    expected_following = f"Following: {i['followingCount']}\n"
                    expected_followers = f"Followers: {i['followersCount']}\n"
                    expected_note_counts = f"Total notes: {i['notesCount']}\n"
                    expected_2fa_stats = f"Two Factor Enable: {i['twoFactorEnabled']}\n"
                    expected_password_stats = \
                        f"Enable password-less login?: {i['usePasswordLessLogin']}\n"
                    expected_reply += (expected_name
                                       + expected_username
                                       + expected_user_id
                                       + expected_create_time
                                       + expected_last_update
                                       + expected_description
                                       + expected_birthday
                                       + expected_location
                                       + expected_following
                                       + expected_followers
                                       + expected_note_counts
                                       + expected_2fa_stats
                                       + expected_password_stats
                                       + expected_lnbreak
                                       )
                reply_text = expected_title + expected_lnbreak + expected_reply + expected_lnbreak
            else:
                reply_text = 'Instance unavailable!'
        except Exception as warning_feedback: #pylint: disable=broad-except
            print(warning_feedback)
            reply_text = 'Instance unavailable!'
    return reply_text
