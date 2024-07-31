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

# GUI
TK_TITLE = "Lancement de FortiVPN"
TK_WIN_WITH = 300
TK_WIN_HEIGHT = 400

TK_ERROR = "Erreur"

# Application
APP_VPN_NAME    = "openfortivpn"    # Le chemin sera cherché par le programme


#
#   Point d'entrée du programme
#
if "__main__" == __name__:
    # On s'assure que l'application est installée sur le poste
    retour = subprocess.run(['which', APP_VPN_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if not retour.returncode == 0:
        #print(f"Erreur - Le module '{APP_VPN_NAME}' n'est pas installé")
        tkMB.showwarning(title=TK_ERROR, message=f"Le module '{APP_VPN_NAME}' n'est pas installé")
        exit(2)

    # Extraction du chemin complet vers l'application
    buffer = io.StringIO(retour.stdout)
    appPath = buffer.readline() # retrait du sut de ligne final

# EOF
