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
TK_WIN_WITH = 300
TK_WIN_HEIGHT = 400

TK_ERROR    = "Erreur"
TK_WARNING  = "Attention"

# Application et commandes
APP_VPN_NAME    = "openfortivpn"    # Le chemin sera cherché par le programme
CMD_WHICH        = "which"

#
#   Point d'entrée du programme
#
if "__main__" == __name__:
    # On s'assure que l'application est installée sur le poste
    retour = subprocess.CompletedProcess
    try:
        retour = subprocess.run([CMD_WHICH, APP_VPN_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError:
        tkMB.showerror(title=TK_ERROR, message=f"Erreur lors de l'appel de la commande {CMD_WHICH}")
        exit(2)
    except FileNotFoundError:
        tkMB.showerror(title=TK_ERROR, message=f"La commande '{CMD_WHICH}' est introuvable")
        exit(2)

    if not retour.returncode == 0:
        #print(f"Erreur - Le module '{APP_VPN_NAME}' n'est pas installé")
        tkMB.showwarning(title=TK_WARNING, message=f"Le module '{APP_VPN_NAME}' n'est pas installé")
        exit(3)

    # Extraction du chemin complet vers l'application
    buffer = io.StringIO(retour.stdout)
    appPath = buffer.readline() # retrait du sut de ligne final
    #print(appPath)


# EOF
