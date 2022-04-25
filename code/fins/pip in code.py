import pip


def Pip_Install(name_package):
    """
    pip install a package python
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
    while True:
        name_package = input("Enter name for package python\n ->")
        Pip_Install(name_package)


if __name__ == '__main__':
    main()
