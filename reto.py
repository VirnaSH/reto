
file = open("raw-text.txt", "r")
date = file.read()
file.close()

 
class PreprocesarTexto():
    def __init__(self,text):
        formatted_text =text.replace(",","").replace(".","").replace("!","")
        self.fmt_text= formatted_text.lower()
        print(self.fmt_text)

    def freq_all(self):
        #tokenizar
        print("Texto:", self.fmt_text)
        wordList = self.fmt_text.split(" ")
        print("Tokens:", wordList)

        frequency_map = {}
        Word_set = set(WordList)
        for Word in Word_set:
            if WordList.count(Word) == 1:
                frequency_map[Word] = WordList.count(Word)
        return frequency_map
    
    

# reto = PreprocesarTexto(date)
# print(reto.frecuencias_todo())


analized = PreprocesarTexto(date)
analized.freq_all
