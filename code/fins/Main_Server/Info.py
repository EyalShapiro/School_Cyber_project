import os
import sys
from sys import *

from libcst import In


class Info:  # אין פעולה בונה

    def Get_Platform_PC():
        """
    הפעולה מחזירה את סוג מערכת הפעלה
    ואת גרסת מערכת הפעלה בשימוש
        """
        import sysconfig
        return sysconfig.get_platform()

    def Cores_Computer():
        ''' 
        הפעולה מחזירה את מספר המעבדים שבמערכת.
        מחזירה ללא אם לא נקבע
        '''
        return os.cpu_count()

    def Get_Python_Version():
        """
        הפעולה מחזירה את גרסת פייתון שאתה משתמש 
        (3.7.4) בצורה הבאה
        """
        # this_py = sys.version_info
        this_py = sys.version_info.major, sys.version_info.minor, sys.version_info.micro
        return this_py

    def Check_Python_Version(py_version):
        """
        פעןלה מקבלת גרסת פייתון מסוגה
        ("3.7")בצורה הבעה str 
                ובדוקת בעזרת פייתון את גירסת פייתון 
       True האם  גדולה יותר מגרסה שקיבלנו היא מחזר 
        False  אחרת 
        """
        version = py_version.split('.')  # הגרסה שקיבלנו
        this_py = Info.Get_Python_Version()  # הגרסה שך המחשב

        if int(version[0]) > int(this_py[0]):
            return True
        elif int(version[0]) == int(this_py[0]) and int(version[1]) > int(this_py[1]):
            return True
        elif int(version[0]) == int(this_py[0]) and int(version[1]) == int(this_py[1]) and int(version[2]) >= int(this_py[2]):
            return True
        else:
            return False

    def Pip_Install(name_package):
        """
        pip install a python3 packages
        name_package[str]: שם של החבילה
        הפעולה מחזר טקסט שכל מה שקוא בשורת הפקודה

        """
        return os.system('pip install '+str(name_package))

    def Install_in_File(file_name):
        """
        מקבלת שם קובץ ומוסיפה את כל ספריות בתוכו
        הפעולה מחזר רשימה שכל מה שקוא בשורת הפקודה

        """
        file_lines = [x.rstrip() for x in open(file_name)]
        for i in file_lines:
            Info.Pip_Install(i)
        print('fins install')

    def Get_Size_File(filename):
        """
        הפעולה מקבלת קובץ
        הפעולה מחזירה את גודל קובץ 
        """
        file_size = os.stat(filename)
        return file_size



