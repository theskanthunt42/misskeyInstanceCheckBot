"""Search blocked domains by a Misskey Instance"""
import requests

def Main(command_string):  #pylint: disable=invalid-name
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
        return f"Instances suspended by {instance_url}:\n\n" + reply_text

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except
