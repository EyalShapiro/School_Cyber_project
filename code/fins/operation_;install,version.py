import pip
import platform

from pip import _internal


def Operating_System():
    """
    הפעולה מחזירה את סוג מרחת הפעלה
    וגרסה של מרחת הפעלה שאת משתמש
    """
    return platform.system() + platform.release()


def GET_Python_Version():
    """
    הפעולה מחזירה את גרסת פייתון שאת משתמש
    """
    return platform.python_version()


def GET_List_Install():
    # מהציג את כל החבילות המותקנות
    list_internal = _internal.main(['list'])
    return list_internal


def Pip_Install(name_package):
    """
    pip install a python packages
    package[str]: שם של החבילה
    """
    help = 'pip install'

    if (help == name_package[0:len(help)]):
        name_package = name_package[len(help):]
    if hasattr(pip, 'main'):
        pip.main(['install', name_package])
    else:
        pip._internal.main(['install', name_package])


# Example
def main():
    print('Operating System: ' + Operating_System())
    print('Python Version: ' + GET_Python_Version())
    print('all ')
    while True:
        name_package = input("Enter name for package python\n ->")
        Pip_Install(name_package)


if __name__ == '__main__':
    main()
