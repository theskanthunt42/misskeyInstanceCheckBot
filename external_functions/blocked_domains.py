"""Search blocked domains by a Misskey Instance"""
import requests

def Main(command_string): #pylint: disable=invalid-name
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
