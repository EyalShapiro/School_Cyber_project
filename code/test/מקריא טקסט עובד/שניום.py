# Import the required module for text
# to speech conversion
from gtts import gTTS
import os
t = 'FIRST® Robotics Competition combines the excitement of sport with the rigors of science and technology. Teams of students are challenged to design, build, and program industrial-size robots and compete for awards, while they also create a team identity, raise funds, hone teamwork skills, and advance respect and appreciation for STEM within the local community.'
my_text = t
language = 'en'
obj = gTTS(text=my_text, lang=language, slow=False)
name = "Speech"+".mp3"
obj.save(name)
os.system("mpg321 "+name)
