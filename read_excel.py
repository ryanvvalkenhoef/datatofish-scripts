import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk() # Maak een variabele root: een eerste venster

canvas1 = tk.Canvas(root, width=300, height=300, bg = 'lightgray') # Maak een canvas van 300 bij 300
canvas1.pack() # Plaats canvas zonder positie of andere eigenschappen in het venster

def getExcel():
    global df
    df = pd.read_excel (r'.\Daily-SCRUM_Presentielijst.xlsx') # Open het excel bestand in variabele df
    print(df) # Print de data uit het excel bestand

# Maak een button en zorg dat getExcel() wordt uitgevoerd als erop geklikt wordt
browseButton_Excel = tk.Button(text='Toon presentielijst', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel) # Maak een venster van 150 bij 150 met de button erin

root.mainloop() # Stop het python programma