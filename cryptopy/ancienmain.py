import tkinter as tk
import requests, json
from cryppy_coins import get_rank_by_money
from tkinter import *


#creer une premiere fenetre
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame_principale()
        self.frame_menu_crypto()



    def frame_principale(self):
        self.textePrincipale = tk.Label(self, text="hey")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit, )
        self.textePrincipale.place(height=30, width=30, x=520, y=400)
        self.textePrincipale.place(x=500, y=200)
        self.bouton.pack()

    #creation de la frame pour le menu des choix des crypto
    def frame_menu_crypto(self):
        #creation de la frame de menu
        self.frame1 = Frame(self, relief=FLAT, bg="#878993")
        self.frame1.pack( fill=X, side=LEFT)

        #creation de la frame pour le texte du haut + texte

        self.frame2 = Frame(self.frame1, bg="#878993")
        self.texte_bienvenue =Label(self.frame2, text="Bienvenue sur cryptopy",padx=10, pady=10, bg="#878993")
        self.texte_bienvenue.pack()
        self.frame2.pack(side=RIGHT)
        self.frame1.update()

        # Récupére la largeur
        ##width = self.frame1.winfo_width()
        # Récupére la hauteur
        ##height = self.frame1.winfo_height()
        ##print(width)
        ##print(height)



        #creation des differents boutons
        self.info = Button(self.frame1, text="information",padx=20, pady=70, bg="#878993", relief=FLAT)
        self.btc_button = Button(self.frame1, text="bitcoin",padx=10, pady=70, bg="#878993", relief=FLAT)
        self.eth_button = Button(self.frame1, text="Ethereum",padx=10, pady=70, bg="#878993", relief=FLAT)
        self.lite_button = Button(self.frame1, text="Litecoin",padx=10, pady=70, bg="#878993", relief=FLAT)

        #positionnement des bouttons
        self.frame2.grid(row=1)
        self.frame2.columnconfigure(0, minsize=200)
        self.info.grid(row=2, sticky='nsew')
        self.btc_button.grid(row=3, sticky='nsew')
        self.eth_button.grid(row=4, sticky='nsew')
        self.lite_button.grid(row=5, sticky='nsew')
        print(self.frame1.grid_size())




    #on recupere le prix du bitcoin
    #def recup_bitcoin(self):
     #   return (get_money_info(money_name="bitcoin"))

if __name__ == "__main__":
    # Création de la fenêtre principal
    window = App()
    window.title("Cyptopy")
    window.geometry("1080x720")
    window.minsize(480, 360)
    window.iconbitmap("assets/bitcoin-4130299_1280.ico")
    window.config(background='#9295A0')

    #lancement de la fenetre
    window.mainloop()