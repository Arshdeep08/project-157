from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title(" Endless Pokemon game")
root.geometry("600x400")

root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))
abra=ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasaur=ImageTk.PhotoImage(Image.open ("bulbasaur.jpg"))
charmander=ImageTk.PhotoImage(Image.open ("charmander.jpg"))
ivysaur=ImageTk.PhotoImage(Image.open ("ivysaur.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open ("paras.jpg"))
persian=ImageTk.PhotoImage(Image.open ("persian.jpg"))
pikachu=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
ratata=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "red", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "red", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = ["abra","bulbasaur","charmander","ivysaur","jigglypuff","kadabra","meowth","nidoking","paras","persian","pikachu","ratata","squirtle"]
power_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,12)
    random_pokemon
    random_pokemon_label["text"] = "Player 1 Dice Random Number : " + str(random_no)
    player1_score = player1_score + random_no
    player_1_score_label["text"] = str(player1_score)

player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

root.mainloop()