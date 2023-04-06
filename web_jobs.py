import webbrowser
import os

def open_facebook():
    webbrowser.open("https://facebook.com")
    
def open_google():
    webbrowser.open("https://google.com")
    
def close_browser():
    browserExe = "chrome.exe"
    os.system("taskkill /f /im " + browserExe)