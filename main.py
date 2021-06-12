import PyPDF2
import pyttsx3
class Reading:
    # Add The Path Of The File
    book = open("C:\\Users\\Arbaz\\Desktop\\Face_Detection.pdf","rb")
    pdfReader=PyPDF2.PdfFileReader(book)
    paged=pdfReader.numPages
    print(paged)
    speak=pyttsx3.init()
    from_page=pdfReader.getPage(1)
    text=from_page.extractText()

    speak.say(text)
    speak.runAndWait()
