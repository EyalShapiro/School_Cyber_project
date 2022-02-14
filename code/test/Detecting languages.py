from google.cloud import translate_v2 as translate

# https://cloud.google.com/translate/docs/basic/detecting-language#detecting_the_language_of_a_single_string
def detect_language(text):
    """Detects the text's language."""

    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print("Text: {}".format(text))
    print("Confidence: {}".format(result["confidence"]))
    print("Language: {}".format(result["language"]))

def main():
    print(detect_language('s'))
if __name__ == '__main__':
    main()