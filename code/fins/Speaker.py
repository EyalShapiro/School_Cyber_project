import win32com.client
import time
speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("---------------------RUN---------------------\n")
print("\t\tTips:In operation,enter 'q' to quit")
while True:
    speak_on = input("\nType in what you want to say:")
    speaker.Speak(speak_on)
    print(speak_on)
    if speak_on == 'q':
        time.sleep(0.5)
        print("\nClosing program......\n")
        speaker.Speak("Closing Program.")
        time.sleep(3)
        print("Program is closing!Thank for you use!")
        speaker.Speak("Program is closing!Thank for you use!")
        break
