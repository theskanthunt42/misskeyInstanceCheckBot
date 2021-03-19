import requests
"""Followers from target fediverse instance"""
"""command: /fedi_follow_by"""
def Main(command_string):
    if len(command_string) <= 17:
        reply_text = 'Invaild instance url!'
    else:
        try:
            instance_url = command_string.split(' ')[-1].split('//')[-1]
            instance_availability = requests.get(f"https://{instance_url}").status_code
            print(f"{instance_availability} {instance_url}")
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/fedration/followers"