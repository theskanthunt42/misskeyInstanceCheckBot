import requests
#https://rosehip.moe/api-doc#operation/users/stats
#https://rosehip.moe/api-doc#operation/users/show
#Command sting should be like:
#/user_stats [username] [api_host] [remote_host](can be None)
#username: sth like 
def main(command_string):
    print(command_string)
    if len(command_string) <= 11 and len(command_string.split(' ')) <= 3:
        reply_text = 'Invaild instance url!'
    else:
        try:
            if len(command_string.split(' ')) <= 3:
                username = command_string.split(' ')[-2]
                instance_url = command_string.split(' ')[-1].split('//')[-1]
            else:
                username = command_string.split(' ')[-3]
                instance_url = command_string.split(' ')[-2].split('//')[-1]
                remote_instance_url = command_string.split(' ')[-1].split('//')[-1]
            instance_availability = requests.get(f'https://{instance_url}/').status_code
            print(f'{instance_availability} {instance_url}')
            if instance_availability == 200:
                get_user_id_api = f'https://{instance_url}/api/users/show'
                get_user_id_payload = '{"username":"{}"}'.format(username)
                try:
                    userid_api_result = requests.post(get_user_id_api, data=get_user_id_payload)
                    if userid_api_result.status_code == 200:
                        userid_api_success = True
                except Exception as warning_feedback:
                    uid_get_success = False
                    print(warning_feedback)
                    reply_text = 'Fatal error(Check your username, or instance unavaukable)'
                if userid_api_success:
                    get_uid = userid_api_result.json()
                    userid = get_uid['userId']
                    api_target = f'https://{instance_url}/api/users/stats/'
                    if len(command_string.split(' ')) <= 3:
                        #Default to local instance
                        api_payload = '{"userId":"{}"}'.format(userid)
                        is_remote_user = False
                    else:
                        #Remote user
                        api_payload = '{"userId":"{}", "host":"{}"}'.format(userid, remote_instance_url)
                        is_remote_user = True
                    api_result = requests.post(f'https://{api_target}/api/users/stats', data=api_payload).json()
                    expected_reply = ''
                    expected_title = f'Stats of user {username}'
                    expected_lnbreak = '\n'
                    print(api_result)
                    for i in api_result:
                        expected_name = f'Name: {username}\n'
                        expected_uid = f'userId: {userid}\n'
                        expected_note_counts = f"Notes count: {i['notesCount']}\n"
                        expected_reply_counts = f"Replies count: {i['repliesCount']}\n"
                        expected_renote_counts = f"Renotes count: {i['renotesCount']}\n"
                        expected_begin_renoted = f"Count of begin renoted: {i['renotedCount']}\n"
                        expected_votes_count = f"Votes: {i['pollVotesCount']}\n"
                        expected_voted_count = f"Voted: {i['[pollVotedCount']}\n"
                        expected_local_foers = f"Local followers: {i['localFollowersCount']}\n"
                        expected_local_following = f"Local following: {i['localFollowingCount']}\n"
                        expected_remote_foers = f"Remote followers: {i['remoteFollowersCount']}\n"
                        expected_remote_following = f"Remote following: {i['remoteFollowingCount']}\n"
                        expected_following_count = f"Following: {i['followingCount']}\n"
                        expected_foers_count = f"Followers: {i['followersCount']}\n"
                        expected_sent_reactions = f"Sent reactions: {i['sentReactionsCount']}\n"
                        
