from gtts import gTTS

import playsound

#################################################
loc = "D:\Cyber_project"  # המיקום הקובץ
file_name = "Speech"
text = 'שלום לכולם'

language = 'he'
#################################################


def Text_to_mp3(my_text, language):
    global file_name
    """
    Args:
        text (str): טקס לקריאה
        language (str) : השפה
        return
        True :הקראה נשמרה בהצלחה
        False : שם הקובץ שגוי או סוג שלו ,לא הצליח לשמור
    """
    obj = gTTS(text=my_text, lang=language, slow=False)
    file_name = file_name + ".mp3"
    try:
        obj.save(file_name)
        return True
    except:
        # שם הקובץ שגוי או סוג שלו
        print("The file name is incorrect or its type")
        return False


def open_Speech():
    playsound.playsound(loc)


def main():
    global text, language
    print("The text that happened : \t\n" + text)
    open(Text_to_mp3(text, language))


if __name__ == '__main__':
    main()
