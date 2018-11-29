'''   '''
import serial
import io
import Window_Operations
from tkinter import *
from tkinter.ttk import *

class Window(Frame):

	red = "#ff4d4d"
	green = '#ffff66'
	blue = '#3385ff'
	one_count = 0
	two_count = 0
	three_count = 0
	
	output_str = 'foobar'

	#Fill list
	fill_list = []
	
	#port
	port = serial.Serial(port="/dev/ttyAMA0",
                     baudrate=9600,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS)

	

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#Window Design
		self.style = Style()
		self.style.theme_use("default")

		#Title
		self.master.title("Mixer Application")
		self.pack(fill=BOTH, expand=1)
	
		#Canvas, Cup Image
		#Canvas
		canvas = Canvas(self, width=250,height=280)
		canvas.pack(side='left')

		canvas.create_line(20,50,20,250,width=4,fill="black")
		canvas.create_line(230,50,230,250,width=4,fill="black")
		canvas.create_line(20,250,230,250,width=4,fill="black")
							   #x1, y1, x2, y2
		self.rect_one = canvas.create_rectangle(30,245,220,215,fill="white")
		self.rect_two = canvas.create_rectangle(30,212,220,182,fill="white")
		self.rect_three = canvas.create_rectangle(30,179,220,149,fill="white")
		self.rect_four = canvas.create_rectangle(30,146,220,116,fill="white")
		self.rect_five = canvas.create_rectangle(30,113,220,83,fill="white")
		self.rect_six = canvas.create_rectangle(30,80,220,50,fill="white")


		#Fluid Elements
	
		#Fluid One
		self.fluid_one_label = Label(self, text="Fluid One", foreground=self.red)
		self.fluid_one_label.place(x=300,y=140)

		self.fluid_one_count = Label(self, text=self.one_count)
		self.fluid_one_count.place(x=323,y=165)

		self.fluid_one_btn_up = Button(self, text="↑", command=self.update_count_up_fluid_one)
		self.fluid_one_btn_up.place(x=295,y=190)

		self.fluid_one_btn_down = Button(self, text="↓", command=self.update_count_down_fluid_one)
		self.fluid_one_btn_down.place(x=295,y=216)

		#Fluid Two
		self.fluid_two_label = Label(self, text="Fluid two", foreground=self.green)
		self.fluid_two_label.place(x=400,y=140)

		self.fluid_two_count = Label(self, text=self.two_count)
		self.fluid_two_count.place(x=423,y=165)

		self.fluid_two_btn_up = Button(self, text="↑", command=self.update_count_up_fluid_two)
		self.fluid_two_btn_up.place(x=395,y=190)

		self.fluid_two_btn_down = Button(self, text="↓", command=self.update_count_down_fluid_two)
		self.fluid_two_btn_down.place(x=395,y=216)

		#Fluid Three
		self.fluid_three_label = Label(self, text="Fluid three", foreground=self.blue)
		self.fluid_three_label.place(x=500,y=140)

		self.fluid_three_count = Label(self, text=self.three_count)
		self.fluid_three_count.place(x=523,y=165)

		self.fluid_three_btn_up = Button(self, text="↑", command=self.update_count_up_fluid_three)
		self.fluid_three_btn_up.place(x=495,y=190)

		self.fluid_three_btn_down = Button(self, text="↓", command=self.update_count_down_fluid_three)
		self.fluid_three_btn_down.place(x=495,y=216)

		#Close Button
		btn_close = Button(self, text='Close', command=Window_Operations.exit)
		btn_close.place(x=20,y=360)

		#Reset Button
		btn_reset = Button(self, text='Reset', command=lambda: self.reset(canvas))
		btn_reset.place(x=440,y=360)

		#Make Button
		btn_make = Button(self, text='Make', command=lambda: self.set_fill_list(canvas))
		btn_make.place(x=520,y=360)
		
		#Update for display
		#self.update()
	def test_max(self):
		if (self.one_count + self.two_count + self.three_count) >= 6:
			return True
		else:
			return False

	def update_count_up_fluid_one(self):
		if self.test_max() == False:
			self.one_count += 1
			self.fluid_one_count.configure(text=self.one_count)

	def update_count_down_fluid_one(self):
		if self.one_count != 0:
			self.one_count -= 1
			self.fluid_one_count.configure(text=self.one_count)

	def update_count_up_fluid_two(self):
		if self.test_max() == False:
			self.two_count += 1
			self.fluid_two_count.configure(text=self.two_count)

	def update_count_down_fluid_two(self):
		if self.two_count != 0:
			self.two_count -= 1
			self.fluid_two_count.configure(text=self.two_count)

	def update_count_up_fluid_three(self):
		if self.test_max() == False:
			self.three_count += 1
			self.fluid_three_count.configure(text=self.three_count)	

	def update_count_down_fluid_three(self):
		if self.three_count != 0:
			self.three_count -= 1
			self.fluid_three_count.configure(text=self.three_count)

	def set_fill_list(self, canvas):
		self.output_string()
		i = 0
		while i < self.one_count:
			self.fill_list.append(1)
			i += 1
		i = 0
		while i < self.two_count:
			self.fill_list.append(2)
			i += 1
		i = 0
		while i < self.three_count:
			self.fill_list.append(3)
			i += 1
		self.set_fill_color(canvas)
		#print(self.fill_list)
		
	def output_string(self):
                self.output_str = 'a'+str(self.one_count)+'b'+str(self.two_count)+'c'+str(self.three_count)
                print(self.output_str)

	def set_fill_color(self, canvas):
		self.write_to_arduino()
		i = 1 #determines the rectangle
		for e in self.fill_list:
			if e == 1:
				if i == 1:
					canvas.itemconfig(self.rect_one, fill=self.red)
				elif i == 2:
					canvas.itemconfig(self.rect_two, fill=self.red)
				elif i == 3:
					canvas.itemconfig(self.rect_three, fill=self.red)
				elif i == 4:
					canvas.itemconfig(self.rect_four, fill=self.red)
				elif i == 5:
					canvas.itemconfig(self.rect_five, fill=self.red)
				elif i == 6:
					canvas.itemconfig(self.rect_six, fill=self.red)
				i += 1
			elif e == 2:
				if i == 1:
					canvas.itemconfig(self.rect_one, fill=self.green)
				elif i == 2:
					canvas.itemconfig(self.rect_two, fill=self.green)
				elif i == 3:
					canvas.itemconfig(self.rect_three, fill=self.green)
				elif i == 4:
					canvas.itemconfig(self.rect_four, fill=self.green)
				elif i == 5:
					canvas.itemconfig(self.rect_five, fill=self.green)
				elif i == 6:
					canvas.itemconfig(self.rect_six, fill=self.green)
				i += 1				
			elif e == 3:
				if i == 1:
					canvas.itemconfig(self.rect_one, fill=self.blue)
				elif i == 2:
					canvas.itemconfig(self.rect_two, fill=self.blue)
				elif i == 3:
					canvas.itemconfig(self.rect_three, fill=self.blue)
				elif i == 4:
					canvas.itemconfig(self.rect_four, fill=self.blue)
				elif i == 5:
					canvas.itemconfig(self.rect_five, fill=self.blue)
				elif i == 6:
					canvas.itemconfig(self.rect_six, fill=self.blue)
				i += 1
		#Serial stuff goes here
		self.fill_list = []

	def reset(self, canvas):
		canvas.itemconfig(self.rect_one, fill='white')
		canvas.itemconfig(self.rect_two, fill='white')
		canvas.itemconfig(self.rect_three, fill='white')
		canvas.itemconfig(self.rect_four, fill='white')
		canvas.itemconfig(self.rect_five, fill='white')
		canvas.itemconfig(self.rect_six, fill='white')
		
	def write_to_arduino(self):
            self.port.close()
            self.port.open()
            self.port.write(self.output_str.encode())
            self.port.close()
            #print(self.port.write(self.output_str.encode()))

