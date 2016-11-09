from tkinter import *

master = Tk()
master.wm_title("SKings Star")

width = 1000
height = 1000
lineNoInQuarter = 150
lineColor = "#0000FF"

w = Canvas(master, width=width, height=height)
w.pack()

for i in range(0,lineNoInQuarter + 1):
	w.create_line(float((width/2)+(width/(2*lineNoInQuarter))*i),(height/2),(width/2),float(height-(height/(2*lineNoInQuarter))*i), fill=lineColor, width=1)
	w.create_line(float((width/2)-(width/(2*lineNoInQuarter))*i),(height/2),(width/2),float(height-(height/(2*lineNoInQuarter))*i), fill=lineColor, width=1)
	w.create_line(float((width/2)+(width/(2*lineNoInQuarter))*i),(height/2),(width/2),float((height/(2*lineNoInQuarter))*i), fill=lineColor, width=1)
	w.create_line(float((width/2)-(width/(2*lineNoInQuarter))*i),(height/2),(width/2),float((height/(2*lineNoInQuarter))*i), fill=lineColor, width=1)


mainloop()