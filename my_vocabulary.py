import openpyxl
from operator import itemgetter
from tkinter import *

# Load the workbook
file_name = 'akuk_words.xlsx'
wb = openpyxl.load_workbook(file_name)

# Get the active worksheet
ws = wb.active

# Read the data from the worksheet and sort it in Akuk alphabetical order
data = [(row[1].value, row[2].value, row[0].value) for row in ws.iter_rows(min_row=2, values_only=True)]
data.sort(key=itemgetter(0))

# Create a Tkinter window to display the data
window = Tk()
window.title("Akuk Words in Akuk Alphabetical Order")

# Create a table to display the data
table = Frame(window)
table.pack(pady=10, padx=10)

# Create the header row
num_label = Label(table, text="Numeric Value", font=("Arial", 14, "bold"), borderwidth=1, relief="solid", padx=10, pady=5)
num_label.grid(row=0, column=0)
akuk_label = Label(table, text="Akuk Word", font=("Arial", 14, "bold"), borderwidth=1, relief="solid", padx=10, pady=5)
akuk_label.grid(row=0, column=1)
meaning_label = Label(table, text="Meaning", font=("Arial", 14, "bold"), borderwidth=1, relief="solid", padx=10, pady=5)
meaning_label.grid(row=0, column=2)

# Display the data in the table
for i, row in enumerate(data):
    num_label = Label(table, text=row[0], font=("Arial", 12), borderwidth=1, relief="solid")
    num_label.grid(row=i+1, column=0)
    akuk_label = Label(table, text=row[1], font=("Arial", 12), borderwidth=1, relief="solid")
    akuk_label.grid(row=i+1, column=1)
    meaning_label = Label(table, text=row[2], font=("Arial", 12), borderwidth=1, relief="solid")
    meaning_label.grid(row=i+1, column=2)

# Run the Tkinter event loop
window.mainloop()


