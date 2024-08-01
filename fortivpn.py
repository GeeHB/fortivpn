#!/usr/bin/python3
#
# coding=UTF-8
#
#   File        :   fortivpn.py
#
#   Author      :   JHB
#
#   Description :   Ouverture du VPN
#

# Tentative de chargement de tcltk (pour l'interface graphique')
try:
    import tkinter as tk
    from tkinter import ttk
    import tkinter.font as tkFont
    import tkinter.messagebox as tkMB
    import tkinter.filedialog as tkDialog
    import tkinter.scrolledtext as tkScrolledText
except ModuleNotFoundError:
    print("Le module tkinter n'est pas installé")
    exit(1)

import subprocess, io
import os, sys

# Quelques constantes
#

# Cette application ...
APP_NAME = "fortivpn"
APP_RELEASE = "0.1.1"

# GUI
TK_TITLE = f"Lancement de {APP_NAME} v{APP_RELEASE}"
TK_WIN_WITH = 400
TK_WIN_HEIGHT = 500

TK_TAB_CONNECTION   = "Connexion"
TK_TAB_LOGS         = "Sorties"

TK_SERVER_NAME      = "Serveur"
TK_CERT             = "Certificat"
TK_USER_NAME        = "Compte"
TK_USER_PWD         = "Mot de passe"

TK_ERROR    = "Erreur"
TK_WARNING  = "Attention"

# Application et commandes
APP_VPN_NAME    = "openfortivpn"    # Le chemin sera cherché par le programme
CMD_WHICH        = "which"

#
# Fonctions et objets à usage interne
#

# "La" fenêtre
#
class mainFrame():

    # Construction
    def __init__(self, root, bin):

        # Conservation des paramètres
        self.root_ = root
        self.bin_ = bin

        self.connected_ = False # Non connecté

        # Police par défaut ...
        self.ownFont_ = tkFont.nametofont("TkDefaultFont")
        self.ownFont_.configure(family="Arial", weight="normal", size=11)

        # Ajout du gestionnaire d'onglets' ...
        self.tabControl_ = ttk.Notebook(self.root_)

        # ... avec 2 onglets
        self.connectionTab_ = ttk.Frame(self.tabControl_)
        self.tabControl_.add(self.connectionTab_, text = TK_TAB_CONNECTION)

        self.logsTab_ = ttk.Frame(self.tabControl_)
        self.tabControl_.add(self.logsTab_, text = TK_TAB_LOGS)
        self.tabControl_.pack(expand = 1, fill ="both")

        # Onglet "Connexion""
        #

        # Nom du serveur
        ttk.Label(self.connectionTab_, text = f"{TK_SERVER_NAME} :").grid(column=2, row=1, padx = 50)
        self.serverNameEdit_ = ttk.Entry(self.connectionTab_)
        self.serverNameEdit_.grid(column=3, row=1, padx=0, pady=10)

        # Certificat
        ttk.Label(self.connectionTab_, text = f"{TK_CERT} :").grid(column=2, row=2)
        self.CERTEdit_ = ttk.Entry(self.connectionTab_)
        self.CERTEdit_.grid(column=3, row=2, columnspan=3)



        # Nom de l'utilisateur'
        """
        ttk.Label(self.connectTab_, text = f"{TK_USER_NAME} :").grid(column=0, row=1, padx=5, pady=5)
        self.userNameEdit_ = ttk.Entry(self.connectTab_)
        self.userNameEdit_.grid(column=1, row=1, columnspan=8, padx=0, pady=0)

        # Mot de passe
        ttk.Label(self.connectTab_, text = f"{TK_USER_PWD} :").grid(column=0, row=2, padx=5, pady=5)
        self.userPwdEdit_ = ttk.Entry(self.connectTab_)
        self.userPwdEdit_.grid(column=1, row=2, columnspan=8, padx=0, pady=0)
        """
        # Logs
        #
        self.logsEdit_ = tkScrolledText.ScrolledText(self.logsTab_, width=40, height=10)
        self.logsEdit_.grid(row=0, column=0, padx=10, pady=10, sticky="news")

        # Gestion de la retaille
        #
        self.root_.grid_rowconfigure(2, weight=1)
        self.root_.grid_columnconfigure(0, weight=1)

        self.tabControl_.grid_columnconfigure(0, weight=1)
        self.tabControl_.grid_rowconfigure(0, weight=1)

        self.logsTab_.grid_columnconfigure(0, weight=1)
        self.logsTab_.grid_rowconfigure(0, weight=1)

    # Lecture et affichage des valeurs par défaut
    def defautValues(self):
        pass

    # Enregistrement des valeurs saisies
    def saveValues(self):
        pass

    # Deconnexion
    def disConnect(self):
       self.__endConnection()


    #
    # Méthodes internes
    #

    # Lancement de la connexion
    def __startConnection(self):
        pass

    # Fin de la connexion
    def __endConnection(self):
        pass

# _getAppPathName : Recherche du nom complet de l'utilitaire openfortivpn
#
# retour : Nom complet de l'utilitaire ou "" en cas d'erreur
#
def _getAppPathName() -> str:
    retour = subprocess.CompletedProcess
    try:
        retour = subprocess.run([CMD_WHICH, APP_VPN_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError:
        tkMB.showerror(title=TK_ERROR, message=f"Erreur lors de l'appel de la commande {CMD_WHICH}")
        return ""
    except FileNotFoundError:
        tkMB.showerror(title=TK_ERROR, message=f"La commande '{CMD_WHICH}' est introuvable")
        return ""

    if not retour.returncode == 0:
        #print(f"Erreur - Le module '{APP_VPN_NAME}' n'est pas installé")
        tkMB.showwarning(title=TK_WARNING, message=f"Le module '{APP_VPN_NAME}' n'est pas installé")
        return ""

    # Extraction du chemin complet vers l'application
    buffer = io.StringIO(retour.stdout)
    return buffer.readline() # retrait du saut de ligne final

#
#   Point d'entrée du programme
#
if "__main__" == __name__:

    # L'utilisateur courant doit avoir les droit de root (root ou sudoer)


    # On s'assure que l'application est installée sur le poste
    appPath = _getAppPathName()
    if len(appPath) > 0:
        # Elle est correctement installée
        #print(appPath)

        # Création et affichage de la fenêtre
        #
        tkRoot = tk.Tk()
        tkRoot.geometry(f"{TK_WIN_WITH}x{TK_WIN_HEIGHT}")
        tkRoot.title(TK_TITLE)

        # Le contenu
        myFrame = mainFrame(tkRoot, appPath)
        myFrame.defautValues()  # Mise à jour des valeurs par défaut

        # Gestion des évènements
        tkRoot.mainloop()

        # Deconnexion (si nécessaire)
        myFrame.disConnect()

        # Enregistrement des valeurs saisies
        myFrame.saveValues()


# EOF
