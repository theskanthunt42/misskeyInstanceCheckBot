"""Getting user's status from remote instance"""
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
        origin_uid = requests.post(f"https://{origin_instance}/api/users/show", data=api_payload).json()['id']

        # Load user stats json (FINALLY!!!!!!!1111!!!!)
        api_payload = f"{{\"userId\": \"{origin_uid}\"}}"
        user_stats = requests.post(f"https://{origin_instance}/api/users/stats", data=api_payload).json()

        # Format user stats json
        expected_reply = (f"Stats of user {origin_username}\n\n"
                            + f'Name: {origin_username}\n'
                            + f'userId: {origin_uid}\n'
                            + f"Notes count: {user_stats['notesCount']}\n"
                            + f"Replies count: {user_stats['repliesCount']}\n"
                            + f"Replied count: {user_stats['repliedCount']}\n"
                            + f"Renotes count: {user_stats['renotesCount']}\n"
                            + f"Count of begin renoted: {user_stats['renotedCount']}\n"
                            + f"Votes: {user_stats['pollVotesCount']}\n"
                            + f"Voted: {user_stats['pollVotedCount']}\n"
                            + f"Local followers: {user_stats['localFollowersCount']}\n"
                            + f"Local following: {user_stats['localFollowingCount']}\n"
                            + f"Remote followers: {user_stats['remoteFollowersCount']}\n"
                            + f"Remote following: {user_stats['remoteFollowingCount']}\n"
                            + f"Following: {user_stats['followingCount']}\n"
                            + f"Followers: {user_stats['followersCount']}\n"
                            + f"Sent reactions: {user_stats['sentReactionsCount']}\n"
                            + f"Received reactions: {user_stats['receivedReactionsCount']}\n"
                            + f"Drive files count: {user_stats['driveFilesCount']}\n"
                            + f"Drive usage: {utils.filesize(user_stats['driveUsage'])}\n")
        # Return Generated content
        return expected_reply

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return debug_msg + warning_feedback  #pylint: disable=broad-except
