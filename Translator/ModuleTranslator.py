from googletrans import Translator

MyTranslator = Translator()
def Translate(Text : str, TargetLang : str = 'ko') -> str:
	return MyTranslator.translate(text=Text, dest=TargetLang).text