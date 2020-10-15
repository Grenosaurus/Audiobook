# audiobook
Simple audiobook that ha three different modes to operate. This program uses both the python's text-to-speech and win32 communication object to read the selected PDF file.

If a audio file is needed then the program also uses Google text-to-speech module for generating the .mp3 audio file of the PDF text. Reason why we use gTTS for creating a audio file is due to the current version of pyttsx3 has lots of errors and the version used in this program does not have the audio file creation function.

Module dependencies can be found in requirments text file.

# How to Use
Program will open up user's file explorer for the user to select the PDF file that they want to use for reading or generating a audio file for later usage. The gTTS module will need a internet connection for creating the audio file and also with larger PDF files this will also take some time.
