import googletrans
from gtts import gTTS
from gtts import *
import os
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

###########################################
dict_language = googletrans.LANGUAGES  # Dictionaries_Language
translator = googletrans.Translator()
###########################################


# # הגש בקשה לגוגל כדי לקבל סינתזה
# tts = gtts.gTTS("Hello world")
# # שמור את קובץ השמע
# tts.save("hello.wav")
# # הפעל את קובץ האודיו
# playsound("hello.wav")


# # all available languages along with their IETF tag
# print(gTTS.lang.tts_langs())

def Identifies_Languages(text):
    """
    הפעולה מקבלת טקסט ומחזיר את מפתח השפה 
    """
    return googletrans.Translator().detect("hello world!").lang


class Text_To_Speech:
    def __init__(self, text, location='code/fins/Main_Server', file_name='say.wav'):
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
        self.location = location
        self.language = Identifies_Languages(text)

    def Get_File_Name(self):  # מחזיר את שם הקובץ
        return self.file_name

    def Set_Location(self, language):  # עדקן מיקום הקובץ
        self.language = language

    def Set_text(self, text):  # העדכון טקסט
        self.text = text
        self.language = Identifies_Languages(text)

    def Get_text(self):  # החזרת טקסט
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
        """
        פותח את קובץ 
        """
        os.system(self.location+self.file_name)

    def Find_Language_key(self, name_language):
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

    def Get_Num_Languages(self):
        """
          הפעולה מחזירה את מספר השפות שיש בספירה 
        """
        global dict_language
        return len(dict_language)

    def Translator_Text(self, language):
        """
        הפעולה מחקבלת שפה ומתרגמת את טקסט 
        הוא מחזר את טקסט מתוגם לאותו שפה 
        """
        global translator
        self.language = language
        result = translator.translate(self.text, language)
        self.text = result.text
        return self.text
#################################################


def main():
    loc = 'code/fins/Main_Server/'
    s = Text_To_Speech('text', loc)
    s.Save_Speech()
    s.Open_Sound()
    print(s.Translator_Text('he'))
    print(s.Find_Language_key('hebrew'))


if __name__ == '__main__':
    main()
