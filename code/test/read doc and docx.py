import docx


def Docx_File(n):
    """
    מקבלת את שם הקובץ עם הסיומת
    doc or docx הפעולה קורא את המידע של הקובץ
    str  ומחזריה אותו בתור
    """
    data_str = ''
    l = n.split('.')

    if l[-1] != 'doc' and l[-1] != 'docx':
        return 'This is Not a correct file'
    doc = docx.Document(n)

    all_paras = doc.paragraphs
    for pageObj in all_paras:
        t = pageObj.text
        data_str += t+'\n'
    return data_str


print(Docx_File('code/fins/test.doc'))
print(Docx_File('code/fins/test.docx'))
