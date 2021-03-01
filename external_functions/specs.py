"""requests has already included json, an independent json library become no longer compulsory"""
import requests

def Main(command_string):
    """
    Function to generate expected reply text to /about {instance}
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
                api_target = f"https://{instance_url}/api/server-info/"
                api_result = requests.post(api_target).json()
                print(api_result)

                expected_title = f"Specifications of {instance_url}:\n\n"
                expected_cpu = f"Processor: {api_result['cpu']['model']}\n"
                expected_ram = f"Installed RAM: {api_result['mem']['total']}Bytes\n"
                expected_diskspace = f"Storage capacity: {api_result['fs']['total']}Bytes\n"
                expected_diskused = f"Storage used: {api_result['fs']['used']}Bytes\n"

                reply_text = (expected_title
                                + expected_cpu
                                + expected_ram
                                + expected_diskspace
                                + expected_diskused
                )
        except Exception as warning_feedback:
            print(warning_feedback)
            reply_text = "Instance unavailable!"
    return reply_text
