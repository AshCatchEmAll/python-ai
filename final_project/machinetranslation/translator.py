'''Translator module containg french ans english translations'''
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    is_upper=False
    all_caps=False
    if english_text[0].isupper():
        is_upper=True
        if english_text.isupper():
            all_caps=True
        english_text=english_text.lower()
    french_text = MyMemoryTranslator(source="en", target="fr").translate(english_text)
    if all_caps:
        french_text=french_text.upper()
    elif is_upper:
        french_text=french_text.capitalize()
    return french_text

def french_to_english(french_text):
    english_text = MyMemoryTranslator(source = "fr",target = "en").translate(french_text)
    return english_text
    
