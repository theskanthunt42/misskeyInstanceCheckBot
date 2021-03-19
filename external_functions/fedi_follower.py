import requests
"""Followers from target fediverse instance"""
"""command: /fedi_follow_by
command in:
/fedi_follow_by <follows to instance> <follows from instance>
"""
def Main(command_string):
    if len(command_string) <= 17:
        reply_text = 'Invaild instance url!'
    else:
        try:
            from_instance_url = command_string.split(' ')[-1].split('//')[-1] #arg 2
            to_instance_url = command_string.split(' ')[-2].split('//')[-1] #arg 1
            instance_availability = requests.get(f"https://{to_instance_url}").status_code
            print(f"{instance_availability} {to_instance_url}")
            if instance_availability == 200:
                api_target = f"https://{instance_url}/api/fedration/followers"
                api_payload = '{}'