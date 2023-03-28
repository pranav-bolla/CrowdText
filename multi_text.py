# install python
# install vscode
# make folder with code and numbers.txt file
# format for numbers.txt is Name:+1Number (NO EXTRA LINES)
# modify message with your own message

import subprocess
from time import sleep

phone_list = []
names = []

with open("numbers.txt", "r") as f : 
    for line in f.readlines():
        phone_list.append(line.split(':')[1].strip('\n'))
        names.append(line.split(':')[0])

for i in range(len(phone_list)):
    message = f"Good morning {names[i]}!"
    # Construct the AppleScript command
    script = f'tell application "Messages" to send "{message}" to buddy "{phone_list[i]}"'

    # Execute the AppleScript command using subprocess
    subprocess.call(['osascript', '-e', script])
    sleep(1)