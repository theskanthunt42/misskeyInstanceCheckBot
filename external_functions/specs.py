"""requests has already included json, an independent json library become no longer compulsory"""
import requests
from external_functions import utils as convert

def Main(command_string): #pylint: disable=invalid-name
    """
    Function to generate expected reply text to /about {instance}
    Usuage:
    external_functions.func_about.Main({source_command})
    """
    if len(command_string) <= 11:
        reply_text = "Invalid instance url!"
    else:
        try:
            instance_url = command_string.split(" ")[-1].split("//")[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(instance_availability)
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/server-info/"
                api_result = requests.post(api_target).json()
                print(api_result)

                expected_title = f"Specifications of {instance_url}:\n\n"
                expected_cpu = f"Processor: {api_result['cpu']['model']}\n"
                expected_ram = \
                    f"Installed RAM: {convert.filesize(api_result ['mem']['total'])}\n"
                expected_diskspace = \
                    f"Storage capacity: {convert.filesize(api_result['fs']['total'])}\n"
                expected_diskused = \
                    f"Storage used: {convert.filesize(api_result['fs']['used'])}\n"

                reply_text = (expected_title
                                + expected_cpu
                                + expected_ram
                                + expected_diskspace
                                + expected_diskused
                )
        except Exception as warning_feedback:   #pylint: disable=broad-except
            print(warning_feedback)
            reply_text = "Instance unavailable!"
    return reply_text
