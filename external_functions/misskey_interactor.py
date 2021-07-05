"""
Includes functions that interact with Misskey API by sending HTTP requests
"""
import requests
from external_functions import kabaformat

def blocked_domains(command_string): #pylint: disable=invalid-name
    """Search blocked domains by a Misskey Instance"""
    try:
        instance_url = command_string.split(" ")[-1].split("//")[-1]
        api_result = \
            requests.post(f"https://{instance_url}/api/federation/instances/", data='{"blocked":true, "limit":100}').json()
        reply_text = ""
        for api_dict in api_result:
            reply_text += ( f"------- {api_dict['host']} -------\n"
                            f"Description: { api_dict['description']}\n"
                            f"Software: {api_dict['softwareName']}\n"
                            f"Version: {api_dict['softwareVersion']}\n"
                            f"Blocked on: {api_dict['infoUpdatedAt']}\n\n"
            )
        return f"Instances blocked by {instance_url}:\n" + reply_text

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

def list_admins(command_string): #pylint: disable=invalid-name
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

def user_stats(command_string):
    """
    Function for generating user statistics
    """
    try:
        # Command string parser
        debug_msg = "Line 58 - Invalid Input"
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
        user_stats_cache = requests.post(f"https://{origin_instance}/api/users/stats", data=api_payload).json()

        # Format user stats json
        expected_reply = (f"Stats of user {origin_username}\n\n"
                            + f'Name: {origin_username}\n'
                            + f'userId: {origin_uid}\n'
                            + f"Notes count: {user_stats_cache['notesCount']}\n"
                            + f"Received Replys: {user_stats_cache['repliesCount']}\n"
                            + f"Sent Replys: {user_stats_cache['repliedCount']}\n"
                            + f"Sent Renotes: {user_stats_cache['renotesCount']}\n"
                            + f"Count of begin renoted: {user_stats_cache['renotedCount']}\n"
                            + f"Votes: {user_stats_cache['pollVotesCount']}\n"
                            + f"Voted: {user_stats_cache['pollVotedCount']}\n"
                            + f"Local followers: {user_stats_cache['localFollowersCount']}\n"
                            + f"Local following: {user_stats_cache['localFollowingCount']}\n"
                            + f"Remote followers: {user_stats_cache['remoteFollowersCount']}\n"
                            + f"Remote following: {user_stats_cache['remoteFollowingCount']}\n"
                            + f"Following: {user_stats_cache['followingCount']}\n"
                            + f"Followers: {user_stats_cache['followersCount']}\n"
                            + f"Sent reactions: {user_stats_cache['sentReactionsCount']}\n"
                            + f"Received reactions: {user_stats_cache['receivedReactionsCount']}\n"
                            + f"Drive files count: {user_stats_cache['driveFilesCount']}\n"
                            + f"Drive usage: {kabaformat.filesize(user_stats_cache['driveUsage'])}\n")
        # Return Generated content
        return expected_reply

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return debug_msg + warning_feedback  #pylint: disable=broad-except

def top_user(command_string): #pylint: disable=invalid-name
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

def specs(command_string): #pylint: disable=invalid-name
    """
    Function to generate expected reply text to /specs {instance}
    Usage: external_functions.specs.Main(str)
    """
    try:
        instance_url = command_string.split(" ")[-1].split("//")[-1]
        api_result = requests.post(f"https://{instance_url}/api/server-info/").json()
        return (f"Specifications of {instance_url}:\n\n"
                f"Processor: {api_result['cpu']['model']}\n"
                f"Installed RAM: {kabaformat.filesize(api_result ['mem']['total'])}\n"
                f"Storage capacity: {kabaformat.filesize(api_result['fs']['total'])}\n"
                f"Storage used: {kabaformat.filesize(api_result['fs']['used'])}\n"
        )

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

def statistics(command_string): #pylint: disable=invalid-name
    """
    Function to generate expected reply text to /stats {instance}
    Usage: external_functions.statistics.Main(str)
    """
    try:
        instance_url = command_string.split(" ")[-1].split("//")[-1]
        api_result = requests.post(f"https://{instance_url}/api/stats/").json()
        return (f"Statistics of {instance_url}:\n\n"
                f"Global Notes: {api_result['notesCount']}\n"
                f"Local Notes: {api_result['originalNotesCount']}\n"
                f"Discovered users: {api_result['usersCount']}\n"
                f"Local users: {api_result['originalUsersCount']}\n"
                f"Discovered Instances: {api_result['instances']}\n"
                f"Size of cached content of global instances: {api_result['driveUsageRemote']}\n"
                f"Size of content of local instance: {api_result['driveUsageLocal']}\n"
        )

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

def suspended_domains(command_string):  #pylint: disable=invalid-name
    """Search blocked domains by a Misskey Instance"""
    try:
        instance_url = command_string.split(" ")[-1].split("//")[-1]
        api_target = f"https://{instance_url}/api/federation/instances/"
        api_payload = '{"suspended":true, "limit":30}'
        api_result = requests.post(api_target, data=api_payload).json()
        reply_text = ""
        for items in api_result:
            reply_text += ( f"------- {items['host']} -------\n"
                            f"Description: {items['description']}\n"
                            f"Software: {items['softwareName']}\n"
                            f"Version: {items['softwareVersion']}\n"
                            f"Suspended on: {items['infoUpdatedAt']}\n\n"
            )
        return f"Instances suspended by {instance_url}:\n\n{reply_text}"

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except
