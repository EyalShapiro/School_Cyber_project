import os
# open file for reading
file='hello.wav'
f = open(file)

# move file cursor to end
f.seek(0, os.SEEK_END)

# get the current cursor position
print('Size of file is', f.tell(), 'bytes')
