from googletrans import Translator
translator = Translator()


def Translator_Text(text, language):
    global translator
    result = translator.translate(text, language)
    
    return result


def main():
    print(Translator_Text('Mitä sinä teet', 'english'))
    print(Translator_Text('hello', 'he'))

if __name__ == "__main__":
    main()
