from ModuleTranslator import Translate
import pyperclip
# import time
# from threading import Thread
from tkinter import Tk
from tkinter import Text
from tkinter import END

root = Tk()
root.geometry("500x100")
root.wm_attributes("-topmost", 1)

TBox = Text(width=70)
TBox.pack()


LastText = pyperclip.paste()
while True:
	try:
		if LastText != pyperclip.paste():
			LastText = pyperclip.paste()
			TranslatedText = Translate(LastText)

			TBox.delete('1.0', END)
			
			TBox.insert(END, TranslatedText)
			root.deiconify()
	except:
		pass
	root.update()