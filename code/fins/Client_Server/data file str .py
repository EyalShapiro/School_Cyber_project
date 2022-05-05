import PyPDF2


class File_Data():
    def __init__(self, file_name):
        self.file_name = file_name

    def Get_File_Name(self):
        return self.file_name

    def Set_File_Name(self, file_name):
        self.file_name = file_name

    def pdf_file(self):
        """
        מקבלת את שם הקובץ עם הסיומת
            pdf הפעולה קורא את המידע של הקובץ
        str  ומחזריה אותו בתור
        """
        data_str = ''
        l = self.file_name.split('.')
        if l[-1] != 'pdf':
            return 'This is Not a correct file'
        # creating a pdf file object
        pdfFileObj = open(self.file_name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # print(pdfReader.numPages)#מספר עמודים

        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            # extracting text from page
            # print(pageObj.extractText())
            data_str += str(pageObj.extractText())+'\n'
        pdfFileObj.close()
        return data_str

    def txt_file(self):
        """
        מקבלת את שם הקובץ עם הסיומת
        txt הפעולה קורא את המידע של הקובץ
        str  ומחזריה אותו בתור 
        """
        data_str = ''
        l = self.file_name.split('.')
        if l[-1] != 'txt':
            return 'This is Not a correct file'
        with open(self.file_name) as f:
            data_str = f.read()
        return data_str
# לסים את פעולה

    def Read_File(self):
        """
         הפעולה מקבלת שם של קובץ אם סוג שלו ןמחזיר אתה
        את תוכן לפי זה שהיא שולח לפעולה אמתימה
         """
        extension = self.file_name.split('.')
        """   switch עובד קמועה
         c/c++(Cpp) ב
        ⇊⇊"""
        switcher = {
            "txt": self.txt_file(),
            "pdf": self.pdf_file()
        }  # סוג קובץ העניין הוא נכון
        return switcher.get(extension[-1], "")  # אחר מחזר תוכן רק


def main():
    txt = File_Data('code\\fins\\test.txt')
    pdf = File_Data('code\\fins\\test.pdf')

    print("txt file :\n", txt.txt_file())
    print("pdf file :\n", pdf.pdf_file())
    print(txt.Read_File())


if __name__ == '__main__':
    main()
