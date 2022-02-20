# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
from googletrans import constants
###########################################
dict_language = constants.LANGUAGES  # Dictionaries_Language
###########################################


def Find_Language(name_language):
    global dict_language  # מילון הם כל השפות
    '''
    name_language[str]= שם של שפה
    הפעולה מחפסת את המפתח של שפה
    return  המפתח
    or  none= אם היא לא מצה
     '''
    list_kes = []
    for kes, language in dict_language.items():
        if language == name_language:
            # מדפיס את מפתח ו את השפה
            list_kes.append(kes)
            print('kes=', kes, ': language=', language)
    if len(list_kes) == 0:
        print('not find thi language'+language)
    return kes


def print_languages_Kes():
    global dict_language  # מילון הם כל השפות
    '''
    הפעולה מדפיס את כל השפות והפתחות
    '''
    print("Languages:")
    for kes, language in dict_language.items():
        print('kes=', kes, ': language=', language)


def main():
    t = Find_Language('hebrew')
    print(t)
    # print_languages_Kes()


if __name__ == '__main__':
    main()
