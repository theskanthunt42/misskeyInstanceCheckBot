"""Placeholder"""
import requests
from external_functions import utils

def main(command_string):
    """
    Function for generating user statistics
    """
    try:
        # Command string parser
        debug_msg = "Line 15 - Invalid Input"
        remote_url = command_string.split(" ")[-1]
        origin_instance = command_string.split(" ")[1].split("@")[-1]
        origin_username = command_string.split(" ")[1].split("@")[-2]

        # User-identifier Receiver
        debug_msg = "Line 21 - Invalid instance url or username"
        if len(command_string.split(" ")) == 2 :
            api_payload = f"{{\"username\": \"{origin_username}\", \"host\": \"{origin_instance}\"}}"
        else: api_payload = f"{{\"username\": \"{origin_username}\", \"host\": \"{remote_url}\"}}"
        origin_uid = \
            requests.post(f"https://{origin_instance}/api/users/show", data=api_payload).json()['id']
        print(remote_url)
        print(origin_username)
        print(origin_instance)
        print(origin_uid)

        # Load user stats json (FINALLY!!!!!!!1111!!!!)
        api_payload = f"{{\"userId\": \"{origin_uid}\"}}"
        user_stats = requests.post(f"https://{origin_instance}/api/users/stats", data=api_payload).json()

        # Fomat user stats json
        expected_reply = ''
        expected_title = f'Stats of user {origin_username}'
        expected_lnbreak = '\n'
        print(user_stats)
        for i in user_stats:
            expected_name = f'Name: {origin_username}\n'
            expected_uid = f'userId: {origin_uid}\n'
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
            expected_drive_usage = f"Drive usage: {utils.filesize(i['driveUsage'])}\n"
            expected_reply += ("\n"
                                + expected_title
                                + expected_name
                                + expected_uid
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

        # Return Generated content
        return expected_reply

    except Exception as warning_feedback:   #pylint: disable=broad-except
        if len(command_string) <= 19:
            print("Invalid input.")
        else:
            print(debug_msg)
            print(warning_feedback)
            return "Error happened!"
