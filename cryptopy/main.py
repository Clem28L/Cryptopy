import tkinter as tk
import requests, json
from cryppy_coins import get_rank_by_money
from tkinter import *
import tkinter.font as font
import os

#creer une premiere fenetre
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame_principale()
        self.frame_menu_crypto()

    #placement du bouton quitter
    def Boutton_quit(self, surface):
        self.bouton = tk.Button(surface, text="Quitter", command=self.quit )
        self.bouton.pack()


    def frame_principale(self):
        #creation de la frame principale
        self.frameprincipale = Frame(self, relief=FLAT, bg="#9295A0")
        self.Boutton_quit(surface=self.frameprincipale)
        self.textePrincipale = tk.Label(self.frameprincipale, text="pagemain")
        self.textePrincipale.pack()
        self.frameprincipale.pack(padx=100, pady=0
                                  , side=RIGHT,expand=YES)


    #creation de la frame pour le menu des choix des crypto
    def frame_menu_crypto(self):
        #creation de la frame de menu
        self.frame1 = Frame(self, relief=FLAT, bg="#878993")
        self.frame1.pack( fill=X, side=LEFT)

        #creation de la Scrollbar


        #creation de la frame pour le texte du haut + texte
        #creation de la font pour le menu
        fontmenu = font.Font(family='Helvetica', size=10)

        self.frame2 = Frame(self.frame1, bg="#878993")
        self.texte_bienvenue =Label(self.frame2, text="Bienvenue sur cryptopy \n veuillez sélectionner la page que vous voulez consulter  " ,padx=10, pady=10, bg="#878993", font=fontmenu)
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

        self.info = Button(self.frame1, text="information",padx=20, pady=70, bg="#878993", relief=FLAT, activebackground="#878993", borderwidth=0, highlightthickness=0, font=fontmenu, command=lambda x=1: window.destroy() & os.system("python main.py") )
        self.btc_button = Button(self.frame1, text="Bitcoin (BTC)",padx=10, pady=70, bg="#878993", relief=FLAT,activebackground="#878993" , borderwidth=0, highlightthickness=0, font=fontmenu, command=lambda x=1: window.destroy() & os.system("python btc.py") )
        self.eth_button = Button(self.frame1, text="Ethereum (ETH)",padx=10, pady=70, bg="#878993", relief=FLAT, activebackground="#878993", borderwidth=0, highlightthickness=0, font=fontmenu, command=lambda x=1: window.destroy() & os.system("python eth.py"))
        self.lite_button = Button(self.frame1, text="Litecoin (LTC)",padx=10, pady=70, bg="#878993", relief=FLAT, activebackground="#878993", borderwidth=0, highlightthickness=0, font=fontmenu, command=lambda x=1: window.destroy() & os.system("python ltc.py"))


        #positionnement des bouttons
        self.frame2.pack(side=TOP)
        self.info.pack()
        self.btc_button.pack()
        self.eth_button.pack()
        self.lite_button.pack()
        print(self.frame1.grid_size())




        #on recupere le prix du bitcoin
        def recup_bitcoin(self):
            return (get_money_info(money_name="bitcoin"))

if __name__ == "__main__":
    # Création de la fenêtre principal
    window = App()
    window.title("Cyptopy")
    window.geometry("1080x720")
    window.resizable(width=False, height=False)
    window.iconbitmap("assets/bitcoin-4130299_1280.ico")
    window.config(background='#9295A0')
    #lancement de la fenetre
    window.mainloop()