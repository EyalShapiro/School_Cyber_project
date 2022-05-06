from gtts import gTTS
import gtts
import os
# # הגש בקשה לגוגל כדי לקבל סינתזה
# tts = gtts.gTTS("Hello world")
# # שמור את קובץ השמע
# tts.save("hello.wav")
# # הפעל את קובץ האודיו
# playsound("hello.wav")


# # all available languages along with their IETF tag
# print(gTTS.lang.tts_langs())


class Text_Speech_class:

    def __init__(self, text, location, language='en', file_name='Speech'):
        '''
        location(str): מיקום הקובץ
        text (str): טקס לקריאה
        language (str) : השפה
        file_name(str): שם הקובץ
        '''
        self.text = text
        self.file_name = file_name
        if location[-1] != "\\":
            location += '\\'
            print(location)
        self.location = location
        self.language = language
    def Set_Language(self,language):
        self.language=language
    def Set_text(self,text):
        self.text=text
    def Get_text(self):
        return self.text
    def Save_Speech(self):
        '''
        הפעולה שמורת את הקובץ לפי  המיקום
        return
        True :הקראה נשמרה בהצלחה
        False : שם הקובץ שגוי או סוג שלו ,לא הצליח לשמור
        '''
        obj = gTTS(text=self.text, lang=self.language, slow=False)
        try:
            obj.save(self.location+self.file_name)
            return True
        except:
            # שם הקובץ שגוי או סוג שלו
            return False

    def Play_Sound(self):
        os.system(self.location+self.file_name)

#################################################


def main():
    loc = 'code/fins/Main_Server/'
    s = Text_Speech_class('text', loc)
    s.Save_Speech()
    s.Play_Sound()


if __name__ == '__main__':
    main()
