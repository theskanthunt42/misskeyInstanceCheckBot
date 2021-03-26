import requests
import external_functions.utils
#https://rosehip.moe/api-doc#operation/users/stats
#https://rosehip.moe/api-doc#operation/users/show
#Command sting should be like:
#/user_stats [username] [api_host] [remote_host](can be None)
#username: sth like syuilo
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
                get_user_id_payload = f'{"username":"{username}"}'
                try:
                    userid_api_result = requests.post(get_user_id_api, data=get_user_id_payload)
                    if userid_api_result.status_code == 200:
                        userid_api_success = True
                except Exception as warning_feedback:
                    userid_api_success = False
                    print(warning_feedback)
                    reply_text = 'Fatal error(Check your username, or instance unavaukable)'
                if userid_api_success:
                    get_uid = userid_api_result.json()
                    userid = get_uid['userId']
                    api_target = f'https://{instance_url}/api/users/stats/'
                    if len(command_string.split(' ')) <= 3:
                        #Default to local instance
                        api_payload = f'{"userId":"{userid}"}'
                        is_remote_user = False
                    else:
                        #Remote user
                        api_payload = f'{"userId":"{userid}", "host":"{remote_instance_url}"}'
                        is_remote_user = True
                    api_result = requests.post(f'https://{api_target}/api/users/stats', data=api_payload).json()
                    expected_reply = ''
                    expected_title = f'Stats of user {username}'
                    expected_lnbreak = '\n'
                    print(api_result)
                    for i in api_result:
                        expected_name = f'Name: {username}\n'
                        expected_uid = f'userId: {userid}\n'
                        expected_remo_user = f'Is remote user? {is_remote_user}\n'
                        expected_note_counts = f"Notes count: {i['notesCount']}\n"
                        expected_reply_counts = f"Replies count: {i['repliesCount']}\n"
                        expected_replied_counts = f"Replied count: {i['repliedCount']}\n"
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
                        expected_recv_reactions = f"Received reactions: {i['receivedReactionsCount']}\n"
                        expected_files_count = f"Drive files count: {i['driveFilesCount']}\n"
                        expected_drive_usage = f"Drive usage: {external_functions.utils.filesize(i['driveUsage'])}\n"
                        expected_reply += ("\n"
                                            + expected_name
                                            + expected_uid
                                            + expected_remo_user
                                            + expected_note_counts
                                            + expected_reply_counts
                                            + expected_replied_counts
                                            + expected_renote_counts
                                            + expected_begin_renoted
                                            + expected_votes_count
                                            + expected_voted_count
                                            + expected_local_foers
                                            + expected_local_following
                                            + expected_remote_foers
                                            + expected_remote_following
                                            + expected_following_count
                                            + expected_foers_count
                                            + expected_sent_reactions
                                            + expected_recv_reactions
                                            + expected_files_count
                                            + expected_drive_usage
                                            + expected_lnbreak
                        )
                    reply_text = expected_title + expected_lnbreak + expected_reply + expected_lnbreak
                else:
                    reply_text = "Can't resolve api."
            else:
                reply_text = 'Instance not available!'
        except Exception as warning_feedback:
            print(warning_feedback)
            reply_text = 'Instance not available!'
    return reply_text
