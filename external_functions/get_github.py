"""
Package: github as interactor
"""
import configparser
import requests
from external_functions import kabaformat

# please uncommand the following 2 lines
# if any keyerror were ocuured within linux during first run
# as the machine is having unknown errors due to OS file reading

# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))

def list_available_repos():
    """
    Return renoted repos as list.
    """
    try:
        config = configparser.ConfigParser()
        config.read('git_resources.ini')
        return kabaformat.list_to_str(config.sections())
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

def api_list_repo(command_string):
    """
    Returns releases of a github repo.
    """
    try:
        str_available_repos = command_string.split(' ')[-1]
        config = configparser.ConfigParser()
        config.read('git_resources.ini')
        releases = requests.get(config[str_available_repos].get('api_resource')).json()['assets']
        feedback = ""
        for builds in releases:
            feedback += (
                f"Discovered releases:\n{builds['name']}\n"
                f"Location:\n{builds['browser_download_url']}\n\n"
            )
        return feedback
    except Exception as warning_feedback: return warning_feedback  #pylint: disable=broad-except

def get_obj_size(command_string):
    """
    Get size of any online onjects.\n
    Returns in bytes in the format of string
    """
    obj_url = command_string.split(" ")[-1].split("//")[-1]
    return requests.get('https://' + obj_url).headers['content-length']
