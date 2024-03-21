from espaco import *
import tkinter as tk

'''
NOTE:
Este main.py desenha direto os pontos no tkinter, sem passar pelas classes do espaco.py.
A ideia seria adicionar os pontos no plano cartesiano puro e o app só atualizar a interface com base no que está lá
'''

class PlanoCartesianoCanvas(tk.Canvas):

    '''
    Canvas do TK correspondente à parte do plano visível. Gerada pelo ChatGPT.
    '''

    def __init__(self, master, plano_logico: PlanoCartesiano, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.origem_x = width / 2
        self.origem_y = height / 2
        self.plano_logico = plano_logico
        self.create_line(0, self.origem_y, width, self.origem_y, fill="black")  # Eixo x
        self.create_line(self.origem_x, 0, self.origem_x, height, fill="black")  # Eixo y

    def plot_ponto(self, ponto: Ponto, cor="black"):
        x, y = ponto.coordenadas
        x_pixel = self.origem_x + x
        y_pixel = self.origem_y - y
        self.create_oval(x_pixel - 1, y_pixel - 1, x_pixel + 1, y_pixel + 1, fill=cor)

class Application(tk.Frame):

    '''
    Aplicação. Gerada pelo ChatGPT.
    '''

    def __init__(self, master: tk.Tk = None):
        super().__init__(master)
        self.master = master
        self.master.title("Plano Cartesiano")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.plano_canvas = PlanoCartesianoCanvas(self, plano_logico=PlanoCartesiano(com_origem=False), width=400, height=400)
        self.plano_canvas.grid(row=0, column=0, padx=10, pady=10)
        self.plotar_ponto_button = tk.Button(self, text="Plotar Ponto", command=self.plotar_ponto)
        self.plotar_ponto_button.grid(row=1, column=0, padx=10, pady=5)
        self.ponto_x_entry = tk.Entry(self)
        self.ponto_x_entry.grid(row=1, column=1, padx=5, pady=5)
        self.ponto_y_entry = tk.Entry(self)
        self.ponto_y_entry.grid(row=1, column=2, padx=5, pady=5)

    def adicionar_ponto(self):
        try:
            x = float(self.ponto_x_entry.get())
            y = float(self.ponto_y_entry.get())
            ponto = Ponto(x, y)
            self.plano_canvas.plano_logico.novo_ponto(x, y)
            self.plano_canvas.plot_ponto(ponto)
        except ValueError:
            tk.messagebox.showerror("Erro", "Coordenadas inválidas. Insira valores numéricos.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()