
import os


def install(pake):
    os.system('pip install '+pake)


def main():
    install('pyaudio')


if __name__ == '__main__':
    main()
