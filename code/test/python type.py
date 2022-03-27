import platform


def Operating_System():
    """
    הפעולה מחזירה את סוג מרחת הפעלה 
    וגרסה של מרחת הפעלה שאת משתמש
    """
    return platform.system() + platform.release()


def Python_Version():
    """
    הפעולה מחזירה את גרסת פייתון שאת משתמש
    """
    return platform.python_version()


def main():
    print('Operating System: ' + Operating_System())
    print('Python Version: ' + Python_Version())


if __name__ == '__main__':
    main()
