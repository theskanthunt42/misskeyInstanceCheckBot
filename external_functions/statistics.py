"""requests has already included json, an independent json library become no longer compulsory"""
import requests

def Main(command_string): #pylint: disable=invalid-name
    """
    Function to generate expected reply text to /stats {instance}
    Usuage:
    external_functions.func_about.Main({source_command})
    """
    if len(command_string) <= 11:
        reply_text = "Invalid instance url!"
    else:
        try:
            dummy_target = command_string.split(" ")[-1]
            instance_url = dummy_target.split("//")[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(instance_availability)
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/stats/"
                api_result = requests.post(api_target).json()
                #Online User Count goes here
                user_api_target = f"https://{instance_url}/api/get-online-users-count/"
                user_api_result = requests.post(user_api_target).json()
                print(api_result)
                print(user_api_result)

                expected_title = f"Statistics of {instance_url}:\n"
                expected_current_online_user = \
                    f"Current online users: {user_api_result['count']}\n"
                expected_global_notes = \
                    f"Global Notes: {api_result['notesCount']}\n"
                expected_local_notes = \
                    f"Local Notes: {api_result['originalNotesCount']}\n"
                expected_global_users = \
                    f"Discovered users: {api_result['usersCount']}\n"
                expected_local_users = \
                    f"Local users: {api_result['originalUsersCount']}\n"
                expected_known_instances  = \
                    f"Discovered Instances: {api_result['instances']}\n"
                expected_global_content = \
                    "Size of cached content of global instances: " \
                    f"{api_result['driveUsageRemote']}\n"
                expected_local_content = \
                    f"Size of content of local instance: {api_result['driveUsageLocal']}\n"

                reply_text = (expected_title
                                + " \n"
                                + expected_current_online_user
                                + expected_global_notes
                                + expected_local_notes
                                + expected_global_users
                                + expected_local_users
                                + expected_known_instances
                                + expected_global_content
                                + expected_local_content
                )
        except Exception as warning_feedback:   #pylint: disable=broad-except
            print(warning_feedback)
            reply_text = "Instance unavailable!"
    return reply_text
