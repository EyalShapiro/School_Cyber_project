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

    def __init__(self, text, locat, language='en', file_name='Speech'):
        '''
        text (str): טקס לקריאה
        language (str) : השפה
        file_name(str): שם הקובץ
        locat(str): מיקום הקובץ
        '''
        self.text = text
        self.file_name = file_name
        self.location = locat
        self.language = language

    # def file_type(self):
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
    def open_Speech(self):
        playsound.playsound(self.locat)

    def save_speech(self):
        '''return
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
