from tkinter import Tk,filedialog,ttk
import pandas as pd

from openpyxl import Workbook, load_workbook
root=Tk()
root.withdraw()
root.attributes('-topmost',True)

filepath =  filedialog.askopenfilenames(filetypes=[("xlsx",".xlsx")])

if filepath:
    print(filepath[0])

    foo = pd.ExcelFile(filepath[0])

    foo2 = pd.read_excel(foo,sheet_name=None)
    print(foo2.keys())


else:
    print("No File Chosen")