import PyPDF2
import docx

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
        type_file = self.file_name.split('.')
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
        return switcher.get(type_file[-1], self.Get_File_Name())
#################################################


def main():
    # txt = File_Data('code/fins/test.txt')
    pdf = File_Data('code/fins/test.pdf')
    # doc = File_Data('code/fins/test.doc')
    docx = File_Data('code/fins/test.docx')
    text = File_Data('text')
    # print("txt file :\n", txt.Txt_File())
    print("pdf file :\n", pdf.Pdf_File())
    # print("doc file :\n", doc.Docx_File())
    print("docx file :\n", docx.Docx_File())

    print(text.Read_Data())
    print(pdf.Read_Data())
    print(docx.Read_Data())


if __name__ == '__main__':
    main()
