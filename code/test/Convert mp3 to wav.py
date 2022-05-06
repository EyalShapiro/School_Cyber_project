
# import required modules
import subprocess

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'hello.mp3',
                 'converted_to_wav_file.wav'])
