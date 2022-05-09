import docx
import PyPDF2
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
    (מזהה את סוג השפה)
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

    def Set_Location(self, language):
        """ הפעולה מקלת שפה או מפתח שפה ועדקן מיקום הקובץ"""
        self.language = language

    def Set_text(self, text):  # העדכון טקסט
        """ הפעולה מקלת טקסט  ועדקן את טקסט"""

        self.text = text
        self.language = Identifies_Languages(text)

    def Get_text(self):  # החזרת טקסט
        return self.text

    def Save_Speech(self):
        '''
        הפעולה שמורת את הקובץ לפי  המיקום
        return
        True :הקראה נשמרה בהצלחה
        False :לא הצליח לשמור
         (שם הקובץ שגוי או סוג שלו )
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
         פותח את קובץ אשמה בתוכנת ברירת מחדל
        """
        f = self.location+self.file_name
        os.system('start ' + f)

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
        הפעולה מדפיס את כל השפות והפתחות שפה
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

class File_Data():
    def __init__(self, file_name=''):
        """        
        file_name(str): שם הקובץ
        """
        self.file_name = file_name

    def Get_File_Name(self):
        """מחזיר את שם קובץ"""
        return self.file_name

    def Set_File_Name(self, file_name):
        """מתקן את שם הקובץ"""
        self.file_name = file_name

    def Pdf_File(self):
        """
        מקבלת את שם הקובץ עם הסיומת
            pdf הפעולה קורא את המידע של הקובץ
        str  ומחזריה אותו בתור
        """
        data_str = ''
        extension = self.file_name.split('.')
        if extension[-1] != 'pdf':
            return 'This is Not a correct file'
        # creating a pdf file object
        pdfFileObj = open(self.file_name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # print(pdfReader.numPages)#מספר עמודים

        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            # extracting text from page
            data_str += str(pageObj.extractText())+'\n'
        pdfFileObj.close()
        return data_str

    def Txt_File(self):
        """
        מקבלת את שם הקובץ עם הסיומת
        txt הפעולה קורא את המידע של הקובץ
        str  ומחזריה אותו בתור
        """
        data_str = ''
        extension = self.file_name.split('.')
        if extension[-1] != 'txt':
            return 'This is Not a correct file'
        with open(self.file_name) as f:
            data_str = f.read()
        return data_str

    def Docx_File(self):
        """
        מקבלת את שם הקובץ עם הסיומת
        doc or docx הפעולה קורא את המידע של הקובץ
        str  ומחזריה אותו בתור
        """
        data_str = ''
        extension = self.file_name.split('.')

        if extension[-1] != 'doc' and extension[-1] != 'docx':
            return 'This is Not a correct file'
        doc = docx.Document(self.file_name)

        all_paras = doc.paragraphs
        for pageObj in all_paras:
            data_str += str(pageObj.text)+'\n'
        return data_str

    def Read_Data(self):
        """
         הפעולה מקבלת שם של קובץ אם סוג שלו ןמחזיר אתה
        את תוכן לפי זה שהיא שולח לפעולה אמתימה
         """
        extension = self.file_name.split('.')
        """   switch עובד קמועה
         c/c++(Cpp) ב
        ⇊⇊"""
        switcher = {
            "txt": self.Txt_File(),
            "pdf": self.Pdf_File(),
            "doc": self.Docx_File(),
            "docx": self.Docx_File()
        }  # סוג קובץ העניין הוא נכון
        # אחר מחזר תוכן רק
        return switcher.get(extension[-1], self.Get_File_Name())
#################################################


def main():
    # txt = File_Data('code/fins/test.txt')
    # pdf = File_Data('code/fins/test.pdf')
    # doc = File_Data('code/fins/test.doc')
    # docx = File_Data('code/fins/test.docx')
    # text = File_Data('text')
    # print("txt file :\n", txt.Txt_File())
    # print("pdf file :\n", pdf.Pdf_File())
    # print("doc file :\n", doc.Docx_File())
    # print("docx file :\n", docx.Docx_File())
    # print(text.Read_Data())

    # loc = 'code/fins/Main_Server/'
    # s = Text_To_Speech('text', loc)
    # s.Save_Speech()
    # print(s.Translator_Text('he'))
    # s.Open_Sound()
    # print(s.Find_Language_key('hebrew'))

    print(text.Read_Data())


if __name__ == '__main__':
    main()
