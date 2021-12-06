import PyPDF2 as pdf
import pyttsx3 as tt

def openfile():
    while True:
        try:
            ui= str(input("Enter PDF path: "))
            f = pdf.PdfFileReader(ui)
        except:
            print("Invalid Entry")
        else:
            print("File Accepted")
            break

    p = f.getPage(0)
    t = p.extractText()
    return t

def speak(text):
    while True:
        try:
            u = str(input("Would you like to save as mp3(y/n): "))
        except:
            print("Invalid Entry")
        else:
            print('File saved as Pdf2Audio.mp3')
            break

    engine = tt.init()
    if u == 'y':
        engine.save_to_file(text, 'Pdf2Audio.mp3')
    engine.say(text)
    engine.runAndWait()



if __name__ == "__main__":
    speak(openfile())