# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
t = 'FIRST® Robotics Competition combines the excitement of sport with the rigors of science and technology. Teams of students are challenged to design, build, and program industrial-size robots and compete for awards, while they also create a team identity, raise funds, hone teamwork skills, and advance respect and appreciation for STEM within the local community.'
# The text that you want to convert to audio
my_text = t

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=my_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
