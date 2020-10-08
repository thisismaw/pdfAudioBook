import pyttsx3
import PyPDF2
#changed Voice per Minute
changedVoiceRate = 130
#asks for the book you want to read
toRead = input("Enter book to read: ")
book = open(toRead+'.pdf','br')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
speaker.setProperty('rate',changedVoiceRate)
#asks for the page of the book
getPage = input("Page: ")
for num in range(int(getPage),pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()