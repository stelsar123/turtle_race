import turtle
import random
import tkinter as tk
from tkinter import *
import pygame
import time

root = Tk()
root.title("Αγώνες με χελώνες!")
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
DICTIONARY = {'red':'κόκκινο', 'green':'πράσινο', 'blue':'μπλε', 'orange':'πορτοκαλί', 'yellow':'κίτρινο', 'black':'μαύρο', 'purple':'μωβ', 'pink':'ροζ', 'brown':'καφέ', 'cyan':'γαλάζιο'}
pygame.mixer.init()

def play():
	pygame.mixer.music.load('data/rocky.wav')
	pygame.mixer.music.play(loops=10)

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Πάμε!')
	color = []
	for var in lista:
		if var.get() == "":
			pass
		else:
			color.append(var.get())
	winner = race(color)
	MyLabel = Label(root, text="Νικήτρια χελώνα είναι αυτή με χρώμα: " + DICTIONARY[winner])
	MyLabel.pack()
	time.sleep(2)
	myButton.config(state=tk.NORMAL)
	screen.clear()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()

lista = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10]
bg = PhotoImage(file='data/tutle.png')
backrnd = Label(root, image=bg)
backrnd.place(x=0,y=0,relwidth=1,relheight=1)
titlos = Label(root, text="Τελικά, μήπως οι χελώνες τρέχουν γρήγορα;;;", font=("Calibri", 20), fg="blue", bg="yellow", padx=50, border=50)
titlos.pack()


label1 = LabelFrame(root,text="Επέλεξε τα χρώματα που θες να αγωνιστούν.", padx=5, pady=10)
label1.pack(padx=30,pady=100)
for j, color in enumerate(COLORS):
	a = Checkbutton(label1, text=DICTIONARY[color], variable=lista[j], onvalue=color, offvalue="")
	a.pack(anchor=W)


myButton = Button(root,width=20,height=5, text="Ξεκίνα τον αγώνα", command=init_turtle, bg="green", fg="white")
myButton2 = Button(root, text="Σταμάτα", command=turtle.bye, bg="red", fg="white")
myButton3 = Button(root, text="Σβήστα όλα", command=turtle.clearscreen, bg="blue", fg="white")
play()
myButton.pack()
myButton2.pack()
myButton3.pack()


root.mainloop()

