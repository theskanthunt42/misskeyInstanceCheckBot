"""requests has already included json, an independent json library become no longer compulsory"""
import requests

def Main(command_string):
    """Search blocked domains by a Misskey Instance"""
    if len(command_string) <= 16:
        reply_text = "Invalid instance url!"
    else:
        try:
            dummy_target = command_string.split(" ")[-1]
            instance_url = dummy_target.split("//")[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(instance_availability)
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/federation/instances/"
                api_payload = '{"blocked":true, "limit":100}'
                api_result = requests.post(api_target, data=api_payload).json()
                expected_reply = ""
                expected_title = f"Instances blocked by {instance_url}:\n"
                expected_lnbreak = " \n"
                for x in range(len(api_result)):

                    expected_host = f"------- {api_result[x]['host']} -------\n"
                    expected_description = f"Description: {api_result[x]['description']}\n"
                    expected_software = f"Software: {api_result[x]['softwareName']}\n"
                    expected_version = f"Version: {api_result[x]['softwareVersion']}\n"
                    expected_block_date = f"Blocked on: {api_result[x]['infoUpdatedAt']}\n"
                    expected_reply += (expected_host
                                        + expected_description
                                        + expected_software
                                        + expected_version
                                        + expected_block_date
                                        + expected_lnbreak)
                reply_text = expected_title + expected_lnbreak + expected_reply
            else:
                reply_text = "Instance unavailable!"
        except Exception as warning_feedback:
            print(warning_feedback)
            reply_text = "Instance unavailable!"
    return reply_text
    