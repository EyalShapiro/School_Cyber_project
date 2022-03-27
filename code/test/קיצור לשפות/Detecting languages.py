# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
from googletrans import constants
###########################################
dict_language = constants.LANGUAGES  # Dictionaries_Language
###########################################
print("Languages:")
for kes, language in dict_language.items():
    print('kes=', kes, ': language=', language)
print('--------------------------------')
for kes, language in dict_language.items():
    if language == 'hebrew':
        print('kes=', kes, ': language=', language)
