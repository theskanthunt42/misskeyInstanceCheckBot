"""Looking for the server specification from given instance"""
import requests
from external_functions import utils as convert

def Main(command_string): #pylint: disable=invalid-name
    """
    Function to generate expected reply text to /specs {instance}
    Usage: external_functions.specs.Main(str)
    """
    try:
        instance_url = command_string.split(" ")[-1].split("//")[-1]
        api_result = requests.post(f"https://{instance_url}/api/server-info/").json()
        return (f"Specifications of {instance_url}:\n\n"
                f"Processor: {api_result['cpu']['model']}\n"
                f"Installed RAM: {convert.filesize(api_result ['mem']['total'])}\n"
                f"Storage capacity: {convert.filesize(api_result['fs']['total'])}\n"
                f"Storage used: {convert.filesize(api_result['fs']['used'])}\n"
        )

    except requests.models.complexjson.decoder.JSONDecodeError: return "Unable to parse data."
    except requests.exceptions.ConnectionError: return "Unable to connect."
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except
