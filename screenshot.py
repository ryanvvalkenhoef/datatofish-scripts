import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk() # Maak een variable root: het eerste venster

canvas1 = tk.Canvas(root, width = 300, height = 300) # Maak een canvas van 300 bij 300
canvas1.pack() # Plaats canvas zonder positie of andere eigenschappen in het venster

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot() # Zet screenshot naar variabele myScreenshot
    file_path = filedialog.asksaveasfilename(defaultextension='.png') # Open dialoogvenster waarin de file_path kan worden geselecteert
    myScreenshot.save(file_path) # Sla het screenshot op naar het pad.

# Maak een button en zorg dat takeScreenshot() wordt uitgevoerd als erop geklikt wordt
myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(150, 150, window=myButton) # Maak een venster van 150 bij 150 met de button erin

root.mainloop() # Stop het python programma