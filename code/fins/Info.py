import multiprocessing
import os
import sys

print(sys.platform)


class Info:
    def Get_Operating_System():
        """
        הפעולה מחזירה את סוג מרחת הפעלה
        וגרסה של מרחת הפעלה שאת משתמש
        """
        return os.cpu_count()

    def Cores_computer():
        ''' 
        הפעולה מחזרה את כמות הליבות במחשב
        '''
        return multiprocessing.cpu_count()

    def Get_Python_Version():
        """
        הפעולה מחזירה את גרסת פייתון שאת משתמש
        """
        return os.system("Python --version")

    def Pip_Install(name_package):
        """
        pip install a python3 packages
        name_package[str]: שם של החבילה
        """
        return os.system('pip install '+str(name_package))

    def This_code_Location():
        """
        הפעולה מחזיר את הנתיב לתוכנית שעכשיו מריצה את הסקריפט
        """
        return sys.executable()


def main():
    # info.Pip_Install(input("Enter name for package python\n ->"))
    print('Operating System: ', Info.Get_Python_Version())
    print("Quantity cores in computer: ", Info.Cores_computer())
    print('Python Version: ', Info.Get_Python_Version())
    print('code_Location: ', Info.mro())


if __name__ == '__main__':
    main()
