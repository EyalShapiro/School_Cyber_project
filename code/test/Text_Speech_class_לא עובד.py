from gtts import gTTS

import playsound


class Speech:

    def file_type(file_name):
        # בודק סוג הקובץ
        file = file_name
        list_type = file.split()
        type = list_type[-1]
        voice_type = ['mp3', 'm4a', 'm4r', 'flac', 'wav']  # כל סוגי קבוצה שלמה
        for i in voice_type:
            if type == i:
                file_name = list_type[0]+'.'+type
        else:
            file_name = list_type[0]+'.mp3'

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

    # def _File_Type(self):
    #     # בודק סוג הקובץ
    #     file = self.file_name
    #     list_type = file.split()
    #     type = list_type[-1]
    #     voice_type = ['mp3', 'm4a', 'm4r', 'flac', 'wav']  # כל סוגי קבוצה שלמה
    #     for i in voice_type:
    #         if type == i:
    #             self.file_name = list_type[0]+'.'+type
    #     else:
    #         self.file_name = list_type[0]+'.mp3'

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
