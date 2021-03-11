"""requests has already included json, an independent json library become no longer compulsory"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """Search blocked domains by a Misskey Instance"""
    if len(command_string) <= 16:
        reply_text = "Invalid instance url!"
    else:
        try:
            instance_url = command_string.split(" ")[-1].split("//")[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(instance_availability)
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/federation/instances/"
                api_payload = '{"blocked":true, "limit":100}'
                api_result = requests.post(api_target, data=api_payload).json()
                expected_reply = ""
                expected_title = f"Instances blocked by {instance_url}:\n"
                expected_lnbreak = " \n"
                for api_dict in api_result:

                    expected_host = f"------- {api_dict['host']} -------\n"
                    expected_description = f"Description: { api_dict['description']}\n"
                    expected_software = f"Software: {api_dict['softwareName']}\n"
                    expected_version = f"Version: {api_dict['softwareVersion']}\n"
                    expected_block_date = f"Blocked on: {api_dict['infoUpdatedAt']}\n"
                    expected_reply += (expected_host
                                        + expected_description
                                        + expected_software
                                        + expected_version
                                        + expected_block_date
                                        + expected_lnbreak)
                reply_text = expected_title + expected_lnbreak + expected_reply
            else:
                reply_text = "Instance unavailable!"
        except Exception as warning_feedback: #pylint: disable=broad-except
            print(warning_feedback)
            reply_text = "Instance unavailable!"
    return reply_text
    