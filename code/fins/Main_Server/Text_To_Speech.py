from gtts import gTTS
import gtts
import os
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
import googletrans
###########################################
dict_language = googletrans.LANGUAGES  # Dictionaries_Language
###########################################


# # הגש בקשה לגוגל כדי לקבל סינתזה
# tts = gtts.gTTS("Hello world")
# # שמור את קובץ השמע
# tts.save("hello.wav")
# # הפעל את קובץ האודיו
# playsound("hello.wav")


# # all available languages along with their IETF tag
# print(gTTS.lang.tts_langs())


class Text_To_Speech:

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

    def Set_Language(self, language):
        self.language = language

    def Set_text(self, text):
        self.text = text

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

    def Open_Sound(self):
        self.Save_Speech()
        os.system(self.location+self.file_name)

    def Find_Language(self,name_language):
        global dict_language  # מילון הם כל השפות
        '''
        name_language[str]= שם של שפה
        הפעולה מחפסת את המפתח של שפה
        return  המפתח
        or  none= אם היא לא מצה
        '''
        list_kes = []
        for kes, language in dict_language.items():
            if language == name_language:
                # מדפיס את מפתח ו את השפה
                list_kes.append(kes)
                print('kes=', kes, ': language=', language)
        if len(list_kes) == 0:
            print('not find thi language'+language)
        return kes


    def print_languages_Kes(self):
        global dict_language  # מילון הם כל השפות
        '''
        הפעולה מדפיס את כל השפות והפתחות
        '''
        print("Languages:")
        for kes, language in dict_language.items():
            print('kes=', kes, ': language=', language)

#################################################


def main():
    loc = 'code/fins/Main_Server/'
    s = Text_To_Speech('text', loc)
    s.Save_Speech()
    s.Open_Sound()


if __name__ == '__main__':
    main()
