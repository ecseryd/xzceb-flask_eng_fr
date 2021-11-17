'''
French-English and English-French translation service
'''
# import json
import os
from ibm_watson import LanguageTranslatorV3 as lt
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

translator = lt(version=VERSION, authenticator=IAMAuthenticator(apikey=apikey))

def englishToFrench(english_text):
    '''
    Translate english_text (a string) into French; return the translation.
    '''
    translator_response = translator.translate(text=english_text, model_id='en-fr')
    french_text = translator_response.get_result()['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    '''
    Translate french_text (a string) into English; return the translation.
    '''
    translator_response = translator.translate(text=french_text, model_id='fr-en')
    english_text = translator_response.get_result()['translations'][0]['translation']
    return english_text


if __name__ == "__main__":
    EN_TEXT = "Good morning, my friend!"
    fr_text = englishToFrench(EN_TEXT)
    new_en_text = frenchToEnglish(fr_text)
    print("English: {}\nFrench: {}\nRetranslation: {}".format(EN_TEXT, fr_text, new_en_text))
