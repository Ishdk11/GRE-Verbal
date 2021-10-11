# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:20:05 2020

@author: Ishan
"""

import random
import tkinter as tk
import xlrd


loc = ("WORDS.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

word_list = []

for i in range(1,sheet.nrows):
    #print(sheet.cell_value(i, 0))
	word_list.append(sheet.cell_value(i, 0))
	
print("Word count is ", len(word_list))
	
def create_msg_box(word):
	tk.messagebox.showinfo("WORD", word)
	
def run_thru_words():
	word = random.choice(word_list)
	word_list.remove(word)
	create_msg_box(word)
	
def words_left():
	print('Words left : ',len(word_list))
	
		
		
	
# creating a main window
main_window = tk.Tk(className = ' GRE WORDS')
main_window.geometry("2040x2040")
main_window.configure(bg = 'green')




# Adding buttons
button_1 = tk.Button(main_window, text = 'NEXT WORD', command = run_thru_words, fg = 'blue')
button_1.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

button_2 = tk.Button(main_window, text = 'WORDS LEFT', command = words_left)
button_2.pack()
#button_1.grid(row = 5, column = 5)
#button_1.pack()

#frame_1.pack()

main_window.mainloop() 
