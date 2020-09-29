import pyttsx3
import PyPDF2

book = open('python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.getNumPages()
print(pages)

page = pdfReader.getPage(20)
text = page.extractText()
print(text)

speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 125)

# speaker.say("Look dear I can speak for you")
# speaker.runAndWait()

for num in range(1, pages):
    page = pdfReader.getPage(num)
    text =  page.extractText()
    speaker.say(text)
    speaker.runAndWait()

print("End")