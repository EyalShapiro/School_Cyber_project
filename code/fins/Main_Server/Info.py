import os
import sys
from sys import *


class Info:
    def Get_Operating_System():
        """
        הפעולה מחזירה את סוג מרחת הפעלה
        וגרסה של מרחת הפעלה שאת משתמש
        """
        return os.cpu_count()

    def Get_Platform_PC():
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

    def Install_in_File(filename):
        """
        מקבלת שם קובץ ומוסיפה את כל ספריות בתוכו
        הפעולה מחזר רשימה שכל מה שקוא בשורת הפקודה
        """
        data = []
        with open(filename) as f:
            data .append(Info.Pip_Install(f.read()))
        return data

    def This_code_Location():
        """
        הפעולה מחזיר את הנתיב לתוכנית שעכשיו מריצה את הסקריפט
        """
        return sys.path()


def main():
    # info.Pip_Install(input("Enter name for package python\n ->"))
    print('file install: ', Info.Install_in_File('test.txt'))
    print('computer Version', Info.Get_Operating_System())
    print("Quantity cores in computer: ", Info.Cores_computer())
    print('Python Version: ', Info.Get_Python_Version())
    print('code_Location: ', Info.This_code_Location())


if __name__ == '__main__':
    main()
