'''   '''

import GUI
import Window_Operations
from tkinter import *
from tkinter.ttk import *


def main():
	#Build Window Obj
	root = Tk()
	root.geometry("620x400+300+300")
	app = GUI.Window()
	root.mainloop()

if __name__ == '__main__':
	main()