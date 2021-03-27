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
        expected_title = f'Stats of user {origin_username}\n'
        expected_lnbreak = '\n'
        print(user_stats)
        expected_name = f'Name: {origin_username}\n'
        expected_uid = f'userId: {origin_uid}\n'
        expected_note_counts = f"Notes count: {user_stats['notesCount']}\n"
        expected_reply_counts = f"Replies count: {user_stats['repliesCount']}\n"
        expected_replied_counts = f"Replied count: {user_stats['repliedCount']}\n"
        expected_renote_counts = f"Renotes count: {user_stats['renotesCount']}\n"
        expected_begin_renoted = f"Count of begin renoted: {user_stats['renotedCount']}\n"
        expected_votes_count = f"Votes: {user_stats['pollVotesCount']}\n"
        expected_voted_count = f"Voted: {user_stats['pollVotedCount']}\n"
        expected_local_foers = f"Local followers: {user_stats['localFollowersCount']}\n"
        expected_local_following = f"Local following: {user_stats['localFollowingCount']}\n"
        expected_remote_foers = f"Remote followers: {user_stats['remoteFollowersCount']}\n"
        expected_remote_following = f"Remote following: {user_stats['remoteFollowingCount']}\n"
        expected_following_count = f"Following: {user_stats['followingCount']}\n"
        expected_foers_count = f"Followers: {user_stats['followersCount']}\n"
        expected_sent_reactions = f"Sent reactions: {user_stats['sentReactionsCount']}\n"
        expected_recv_reactions = f"Received reactions: {user_stats['receivedReactionsCount']}\n"
        expected_files_count = f"Drive files count: {user_stats['driveFilesCount']}\n"
        expected_drive_usage = f"Drive usage: {utils.filesize(user_stats['driveUsage'])}\n"
        expected_reply = ("\n"
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
