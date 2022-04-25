from gtts import gTTS
import gtts
import playsound
from playsound import playsound

# הגש בקשה לגוגל כדי לקבל סינתזה
tts = gtts.gTTS("Hello world")
# שמור את קובץ השמע
tts.save("hello.mp3")
# הפעל את קובץ האודיו
playsound("hello.mp3")


# all available languages along with their IETF tag
print(gtts.lang.tts_langs())

class Text_Speech_class:

    def __init__(self, location, text, language='en', file_name='Speech'):
        '''
        location(str): מיקום הקובץ
        text (str): טקס לקריאה
        language (str) : השפה
        file_name(str): שם הקובץ
        '''
        self.text = text
        self.file_name = file_name
        self.location = location
        self.language = language

    def Save_Speech(self):
        '''
        הפעולה שמורת את הקובץ לפי  המיקום
        return
        True :הקראה נשמרה בהצלחה
        False : שם הקובץ שגוי או סוג שלו ,לא הצליח לשמור
        '''
        obj = gTTS(text=self.text, lang=self.language, slow=False)
        try:
            obj.save(self.file_name)
            return True
        except:
            # שם הקובץ שגוי או סוג שלו
            print("The file name is incorrect or its type")
            return False

    def Play_Sound(self):
        playsound.playsound(self.location)
#################################################


def main():
    loc = 'C:\Eyal\School_Cyber_project'
    s = Speech('text', loc)
    s.Save_Speech()
    s.file_type()
    s.Play_Sound()


if __name__ == '__main__':
    main()
