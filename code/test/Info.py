import pip
from pip import _internal
import platform
import multiprocessing

class info:
    def Get_Operating_System():
        """
        הפעולה מחזירה את סוג מרחת הפעלה
        וגרסה של מרחת הפעלה שאת משתמש
        """
        return platform.system() + platform.release()

    def Cores_computer():
        ''' 
        הפעולה מחזרה את כמות הליבות במחשב
        '''
        return multiprocessing.cpu_count()

    def Get_Python_Version():
        """
        הפעולה מחזירה את גרסת פייתון שאת משתמש
        """
        return platform.python_version()

    def Get_List_Install():
        # מהציג את כל החבילות המותקנות
        return _internal.main(['list'])

    def Pip_Install(name_package):
        """
        pip install a python3 packages
        name_package[str]: שם של החבילה
        """
        help = 'pip install'

        if (help == name_package[0:len(help)]):
            name_package = name_package[len(help):]
        if hasattr(pip, 'main'):
            pip.main(['install', name_package])
            return True
        else:
            _internal.main(['install', name_package])
            return True
        return False


def main():
    # info.Pip_Install(input("Enter name for package python\n ->"))
    print('all packs \n', info.Get_List_Install())
    print('Operating System: ', info.Get_Python_Version())
    print("Quantity cores in computer: ", info.Cores_computer())
    print('Python Version: ', info.Get_Version())


if __name__ == '__main__':
    main()
