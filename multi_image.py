import subprocess
from time import sleep

script = '''
tell application "Messages"
    get id of 1st service
end tell
'''

service_id = subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()


phone_list = []
names = []

with open("numbers.txt", "r") as f : 
    for line in f.readlines():
        phone_list.append(line.split(':')[1].strip('\n'))
        names.append(line.split(':')[0])


image_path = "filename"

your_service_id = service_id 

for i in range(len(phone_list)):
    # Sends image
    script_image = f'''tell application "Messages"
        set theAttachment to POSIX file "{image_path}"
        set theBuddy to buddy "{phone_list[i]}" of service id "{your_service_id}"
        send theAttachment to theBuddy
    end tell'''

    

    # Sends text
    message = f"Good morning {names[i]}!"
    script_text = f'tell application "Messages" to send "{message}" to buddy "{phone_list[i]}"'

    subprocess.call(['osascript', '-e', script_image])
    subprocess.call(['osascript', '-e', script_text])
    sleep(1)