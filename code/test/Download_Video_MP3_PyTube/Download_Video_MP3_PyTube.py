# לא הובד
import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=WH7xsW5Os10")

vids = yt.streams.all()
for i in range(len(vids)):
    print(i, '. ', vids[i])

vnum = int(input("Enter vid num: "))

parent_dir = r"C:"+"\\"+"Eyal\School_Cyber_project"
vids[vnum].download(parent_dir)

# e.g. new_filename.mp3
new_filename = input("Enter filename (including extension): ")

# get default name using pytube API
default_filename = vids[vnum].default_filename
subprocess.run(['ffmpeg', '-i', os.path.join(parent_dir, default_filename),
                os.path.join(parent_dir, new_filename)])

print('done')
