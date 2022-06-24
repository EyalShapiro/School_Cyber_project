import googletrans
from gtts import gTTS
from gtts import *
import os
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

###########################################
dict_language = googletrans.LANGUAGES  # Dictionaries_Language
###########################################


def Identifies_Languages(text):
    """
    הפעולה מקבלת טקסט
    מזהה את שפת הדיבור שבה הטקסט רשום
    ומחזירה את מפתח השפה
    """
    revealed = googletrans.Translator().detect(text).lang
    return revealed


class Text_To_Speech:
    def __init__(self, text, location='/fins/Main_Server/', file_name='say.wav'):
        '''
        location(str): מיקום הקובץ
        text (str): טקס לקריאה
        language (str) : השפה
        file_name(str): שם הקובץ
        '''
        self.text = text
        self.file_name = file_name
        self.location = location
        self.language = Identifies_Languages(text)

    def Get_File_Name(self):
        """
        מחזיר את שם הקובץ
        """
        return self.file_name

    def Get_File_Location(self):
        """
        הפעולה מחזריה את מיקום המאלה של הקובץ
        """
        return self.location+self.file_name

    def Set_Location(self, location):
        """
        הפעולה מקבלת מיקום של הקובץ ומעדכנת אותו
        """
        self.location = location

    def Set_File_Name(self, file_name):
        """
        הפעולה מקבלת שם של הקובץ ומעדכנת אותו
        """
        self.file_name = file_name

    def Set_text(self, text):
        """
         מקבלת טקסט ומעדכנת את text ומעדכנת את השפה
        """
        self.text = text
        self.language = Identifies_Languages(text)

    def Get_text(self):
        """
        מחזיר את הטקסט
        """

        return self.text

    def Save_Speech(self):
        '''
            הפעולה שומרת את הקובץ לפי המיקום
        מחזירה אמת אם הקובץ נשמר בהצלחה  או
        שקר אם היא לא הצליחה לשמור (שם הקובץ שגוי או הסוג שלו)

        '''
        obj = gTTS(text=self.text, lang=self.language)
        try:
            obj.save(self.location+self.file_name)
            return True
        except:
            # שם הקובץ שגוי או סוג שלו
            return False

    def Open_Sound(self):
        """
        הפעולה שמור את הקובץ ואז
        פותח את קובץ אשמה בתוכנת ברירת מחדל
        והם היא מצליחה הפעולה מחזיר אמת
        אחרת שקר
        """
        try:
            self.Save_Speech()
            os.system('start ' + self.location+self.file_name)
            return True
        except:
            print('not')
            return False

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

    def Print_languages_Kes(self):
        global dict_language  # מילון הם כל השפות
        '''
        הפעולה מדפיסה את כל השפות ואת כל מפתחות השפה
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
        translator = googletrans.Translator()
        text_translator = translator.translate(self.text, language)
        self.text = text_translator
        self.language = language
        return text_translator


if __name__ == '__main__':
    # speech = Text_To_Speech('Hello World')
    # speech.Save_Speech()
    # speech.Open_Sound()
    text = 'Eyal '
    print(text, '/t lang', Identifies_Languages(text))
