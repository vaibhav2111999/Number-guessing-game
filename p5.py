# Number-guessing-game
import random
from tkinter import *       #grafical user interface
from tkinter import messagebox

root = Tk()         #creating a instance tk initializes this interpreter and creates the root window.
root.title('Guess the number game')     #Name to the window
root.geometry("400x400")            #dimentions of the window
root['bg'] = 'Blue'                 #color of the window
w = Label(root, text ='RLUES-\n1. Guess the interger number between 0 to 100\n2. If you get the answer within 5 attempts, you will Win! else you will loose', font = "50")  #the text we want to display
w.config(font=('helvetica', 14))        #font of the text
w.pack(pady=30)         #we need to pack the text, unless packing is done we wont be able to see the messagebox

na = Label(root, text='Enter your name')
na.pack(pady=25)
name = Entry(root)
name.pack(pady=20)

an = Label(root, text='Guess a number between 0 to 100:')
an.pack(pady=15)
a = Entry(root)
a.pack(pady=10)

m = random.randint(0,100)       #taking random number between 0 to 100
n = int(m/2)                #for providing hint we divide it by 2
sc = 0         #creating an accumulator to keep number of attempts
print(n)

def guessing():
    global sc       #making accumulator as global so that we can use it in any part of the code
    number = int(a.get())       #Taking the number entered by user and storing it in another variable
    if(n == number):        #comparing if guessed number is equal to the number provided by machine
        s = Label(root, text = 'You got it right')
        s.pack(pady=2)
        result()        #calling result function
    elif(n > number):
        s = Label(root, text = 'The number guessed is too low\nHint:- Multiply your number by 2 times and guess Above it CLICK AGAIN')
        s.after(5000, s.destroy)
        s.pack(pady=2)
        sc += 1
        my_button = Button(root, text = 'click here', command = guessing)   #giving another change to the user to guess it right
    elif(n < number):
        s = Label(root, text = 'The number guessed is too large\nHint:- Divide your number by 2 and guess Below it CLICK AGAIN')
        s.after(5000, s.destroy)
        s.pack(pady=2)
        sc += 1
        my_button = Button(root, text = 'click here', command = guessing)       #giving another change to the user to guess it right
def result():
    if(sc<=4):
        messagebox.showinfo("Results", "You won "+name.get())   #creating a messagebox if the person gets it right within 5 attempts
    else:
        messagebox.showinfo("Results", "You lost it "+name.get() + "Try again")     #creating a messagebox of the results
my_button = Button(root, text = 'click here', command = guessing)       #creating a button widget below the number entry widget and giving the button to move it command to guessing function
my_button.pack(pady=5)      #padding the button

root.mainloop()     #we want the window to retain unless we press close button, hence we loop over and over to keep it on the screen
