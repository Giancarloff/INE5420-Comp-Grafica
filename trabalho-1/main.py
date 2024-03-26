from app import *
from tkinter import *

# Constantes para tamanho da janela
JANELA_LARGURA = 1024
JANELA_ALTURA = 576

# Constantes para o canvas
CANVAS_LARGURA = JANELA_LARGURA
CANVAS_ALTURA = JANELA_ALTURA

# Raiz do Tkinter
ROOT = Tk()
ROOT.title("Sistema Básico de CG 2D")
ROOT.geometry(f"{JANELA_LARGURA}x{JANELA_ALTURA}")

# Canvas principal
CANVAS = Canvas(ROOT, width=CANVAS_LARGURA, height=CANVAS_ALTURA, background="gray")

# Display file
DISPLAY_FILE = DisplayFile(list())

# Aplicação principal
APP = App(ROOT, DISPLAY_FILE, CANVAS)
APP.iniciar()