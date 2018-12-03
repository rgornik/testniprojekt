import Tkinter
import random
import tkMessageBox

secret_num = random.randint(1, 100)

def check_guess():
    user_num = int(guess.get())
    #time.sleep(5)
    if user_num == secret_num:
        tkMessageBox.showerror("Result", "Uganil si")
    else:
        tkMessageBox.showinfo("Result", "Nisi uganil")

main_window = Tkinter.Tk()
#main_window.bind("<Return>", check_guess)

main_window.title("naslov")

greeting_label = Tkinter.Label(main_window, text="Guess the secret number")
greeting_label.pack()

guess = Tkinter.Entry(main_window)
guess.pack()

button = Tkinter.Button(main_window, text="Check", command=check_guess)
button.pack()

main_window.mainloop()