"""Search stats of a Misskey Instance"""
import requests

def Main(command_string): #pylint: disable=invalid-name
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
