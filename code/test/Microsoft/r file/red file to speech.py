# import win32com.client


# def Speaker_text():
#     """
#       יאוצר אוביקת ומחזר את אוביקת
#     """
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")  # מקריעה
#     return speaker


# speaker = Speaker_text()

# file_text = open("text_speech.txt", "r+")
# print(file_text.read())
# string = file_text.read()
# speaker.Speak(string)

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
file = open(
    'C:\Eyal\School_Cyber_project\code\test\Microsoft\r file\text_speech.txt', "r")
text = file.read()
# print(text)
speaker.Speak(text)
file.close()
