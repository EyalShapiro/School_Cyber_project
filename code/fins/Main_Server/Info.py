from fileinput import filename
import os
import sys
from sys import *


class Info:  # אין פעולה בונה
    def Get_Operating_System():
        """
        הפעולה מחזירה את סוג מרחת הפעלה
        וגרסה של מרחת הפעלה שאת משתמש
        """
        return os.cpu_count()

    def Get_Platform_PC():
        """
                הפעולה מחזירה את סוג מערכת הפעלה 
        """
        import sysconfig
        return sysconfig.get_platform()

    def Cores_computer():
        ''' 
        הפעולה מחזר את מספר המעבדים במערכת. מחזירה ללא אם לא נקבע.
        '''
        return os.cpu_count()

    def Get_Python_Version():
        """
        הפעולה מחזירה את גרסת פייתון שאת משתמש
        """
        return os.system("Python --version")

    def Pip_Install(name_package):
        """
        pip install a python3 packages
        name_package[str]: שם של החבילה
        הפעולה מחזר טקסט שכל מה שקוא בשורת הפקודה

        """
        return os.system('pip install '+str(name_package))

    # def Pip_Install_File(file_name):
    #     """
    #     pip install a python3 packages
    #     file_name[str]: שם של קובץ
    #     מוסיף את כל החבילות שני נימצות בקובץ
    #     הפעולה מחזר טקסט שכל מה שקוא בשורת הפקודה

    #     """
    #     return os.system('pip install - r / path/to/'+filename)

    def Install_in_File(file_name):
        """
        מקבלת שם קובץ ומוסיפה את כל ספריות בתוכו
        הפעולה מחזר רשימה שכל מה שקוא בשורת הפקודה

        """
        file_lines = [x.rstrip() for x in open(file_name)]
        for i in file_lines:
            Info.Pip_Install(i)
        print('fins install')
    # def This_code_Location():
    #     """
    #     הפעולה מחזיר את הנתיב לתוכנית שעכשיו מריצה את הסקריפט
    #     """
    #     return sys.path()

    def Get_Size_File(filename):
        """
        הפעולה מקבלת קובץ
        הפעולה מחזר את גודל קובץ
        """
        # open file for reading
        file = open(filename)
        # move file cursor to end
        file.seek(0, os.SEEK_END)
        return file.tell()


def main():

    # info.Pip_Install(input("Enter name for package python\n ->"))
    # print('file install: ', Info.Install_in_File('test.txt'))
    # print('computer Version', Info.Get_Operating_System())
    # print("Quantity cores in computer: ", Info.Cores_computer())
    # print('Python Version: ', Info.Get_Python_Version())
    print('Size of file is', Info.Get_Size_File('hello.wav'), 'bytes')
    # Info.Install_in_File('requirements.txt')
    # print(Info.Get_Platform_PC())


if __name__ == '__main__':
    main()
