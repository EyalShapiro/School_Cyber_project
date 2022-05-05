
import os


def install(pake):
    return os.system('pip install '+str(pake))

def Get_Python_Version():
    """
    הפעולה מחזירה את גרסת פייתון שאת משתמש
    """
    return os.system("Python --version")

def main():
    print(install('pyaudio'))
    print(Get_Python_Version())

if __name__ == '__main__':
    main()
