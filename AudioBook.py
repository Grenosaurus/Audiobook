"""
 Simple python program for personal audiobook (Made: Jauaries).
"""

# Python packets
import PyPDF2
import pyttsx3 # 2.6 version
import time
import os

from win32com.client import Dispatch
from tkinter.filedialog import *
from gtts import gTTS


"""
 Program has three modes:
  1st. Program generates the voice from the win32's communication object and reads the PDF file | If the pyttsx3 module does not work!
  2nd. Google text-to-speech module to generate a audio file from the PDF files text using google's voice | Needs a internet connection!
  3rd. Python's text-to-speech module to generating the PDF text to voice | Does not need internet connection!
 Choose the prefeard mode.
"""


# Generates the voice for the strings | Used by 1st mode
def textVoice(pdf_text):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.speak(pdf_text)


# Reads the book pages
def audioBook():
    book_path = askopenfilename() # Opens the file explorer for selecting a pdf file to read

    # Separates the file name from the path
    drive, path_list = os.path.split(book_path)
    path, file = os.path.split(path_list)
    file_name = file.replace('.pdf','') # Removes the .pdf format from teh file

    pdfReader = PyPDF2.PdfFileReader(book_path) # PDF reader
    page_numbers = pdfReader.numPages # Reads the page numbers of the book
    
    page_start = 0 # Start page
    pdf_text = "" # Empty string to generate to store the entire PDF text
    text_speech = pyttsx3.init()

    # Voice property of pyttsx3 module
    text_speech.setProperty('rate', 150) # voice speed in percentage
    text_speech.setProperty('volume', 0.9)  # Voice volume from 0-1

    # Reading the entire PDF book
    for i in range(page_start, page_numbers):
        page = pdfReader.getPage(i) # Gets the page number
        pdf_text += page.extractText().replace('\n', ' ') # Extracts and stores the text from entire PDF file into one single string variable

    print(pdf_text) # Prints the entire PDF files text in the stored pdf file text page to the terminal (not mandatory)
    
    audio_path = '../Documents/AudioBooks/%s.mp3' % (file_name) # Path to save the audio file | Change this!
    """
    # Uses win32 communicatio module to generate voise | 1st mode
    textVoice(pdf_text) # Reads everyting in the stored string variable
    
    # Generates audio file from the entire PDF file | 2nd mode (needs internet connection)
    google_speaks = gTTS(text = pdf_text, lang = 'en') # Generates Google voice for the PDF
    google_speaks.save(audio_path) # Saves the PDF as audio file
    """
    # Converst the PDF files texts into speech | 3rd mode
    text_speech.say(pdf_text) # Reads the PDF text from the stored strings
    text_speech.runAndWait()
    text_speech.stop()



# Just for fun
def main():

    audioBook()


# Generates teh total time used by the program to complete the task
if __name__ == "__main__":
    # Time of main function
    start_time = time.time() # Start time of the main function
    main()
    end_time = time.time() # End time of the main function

    # Delta time
    Delta_time_seconds = end_time - start_time # Difference between start and end time (defined in seconds)
    Delta_time_minutes = Delta_time_seconds/60 # Difference between start and end time (defined in minutes) | 1 min = 60 s

    # Round value of delta time
    Delta_time_seconds_round = round(Delta_time_seconds, 2)
    Delta_time_minutes_round = round(Delta_time_minutes, 2)

    # Prints the time took for the program to run
    print("\nProgram took %s seconds (~ %s minutes)." % (Delta_time_seconds_round, Delta_time_minutes_round))
