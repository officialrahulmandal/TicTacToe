from tkinter import *
import tkinter.messagebox

# initialising click with True
click = True


# defining a function to update the buttons text and simultaneously checking the winning condition
def check(buttons):
    global click
    print("in check function")
    # updating button text
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        print("in O button")
        click = False
        # checking winning condition
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"
            or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"
            or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"
            or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"
            or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"
            or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"
            or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"
            or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            dashboard.quit()
            tkinter.messagebox.showinfo("congrats X", "player 1 wins this match")
        elif (button1["text"] == button2["text"] == button3["text"] == "O"
              or button4["text"] == button5["text"] == button6["text"] == "O"
              or button7["text"] == button8["text"] == button9["text"] == "O"
              or button1["text"] == button4["text"] == button7["text"] == "O"
              or button2["text"] == button5["text"] == button8["text"] == "O"
              or button3["text"] == button6["text"] == button9["text"] == "O"
              or button1["text"] == button5["text"] == button9["text"] == "O"
              or button3["text"] == button5["text"] == button7["text"] == "O"):
            dashboard.quit()
            tkinter.messagebox.showinfo("congrats O", "player 1 wins this match")
    # updating Button text
    elif buttons["text"] == " " and click == False:
        print("in X button")
        buttons["text"] = "O"
        click = True
        # checking winning condition
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"
            or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"
            or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"
            or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"
            or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"
            or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"
            or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"
            or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            dashboard.quit()
            tkinter.messagebox.showinfo("congrats X", "player 1 wins this match")
        elif (button1["text"] == button2["text"] == button3["text"] == "O"
              or button4["text"] == button5["text"] == button6["text"] == "O"
              or button7["text"] == button8["text"] == button9["text"] == "O"
              or button1["text"] == button4["text"] == button7["text"] == "O"
              or button2["text"] == button5["text"] == button8["text"] == "O"
              or button3["text"] == button6["text"] == button9["text"] == "O"
              or button1["text"] == button5["text"] == button9["text"] == "O"
              or button3["text"] == button5["text"] == button7["text"] == "O"):
            dashboard.quit()
            tkinter.messagebox.showinfo("congrats O", "player 2 wins this match")


    # if none of the above condition satisfied then the match is draw
    else:
        dashboard.quit()
        tkinter.messagebox.showinfo("Draw", "Its A Draw")

# making a tkinter window named Dashboard
dashboard = Tk()
# dashboard.geometry("400x400")
dashboard.title("Tic Tak Toe Game")


# defining some buttons to play
buttons = StringVar()
button1 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button1))
button1.grid(row=0, column=0, sticky=E + W + N + S)
button2 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button2))
button2.grid(row=0, column=1, sticky=E + W + N + S)
button3 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button3))
button3.grid(row=0, column=2, sticky=E + W + N + S)
button4 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button4))
button4.grid(row=1, column=0, sticky=E + W + N + S)
button5 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button5))
button5.grid(row=1, column=1, sticky=E + W + N + S)
button6 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button6))
button6.grid(row=1, column=2, sticky=E + W + N + S)
button7 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button7))
button7.grid(row=2, column=0, sticky=E + W + N + S)
button8 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button8))
button8.grid(row=2, column=1, sticky=E + W + N + S)
button9 = Button(dashboard, font=('Times 26 bold'), text=" ", height=5, width=10, command=lambda: check(button9))
button9.grid(row=2, column=2, sticky=E + W + N + S)
dashboard.mainloop()
