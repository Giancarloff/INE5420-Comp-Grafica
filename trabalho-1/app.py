from model import *
from tkinter import *

class App:

    '''
    Meio de comunicação do modelo com o sistema gráfico.
    Lida com o input do usuário.
    '''

    def __init__(self, root: Tk, display_file: DisplayFile, canvas: Canvas) -> None:
        self.__tk_root = root
        self.__display_file = display_file
        self.__canvas = canvas
        self.__adicionando_reta = False

    @property
    def tk_root(self) -> Tk:
        return self.__tk_root
    
    @property
    def display_file(self) -> DisplayFile:
        return self.__display_file
    
    @property
    def canvas(self) -> Canvas:
        return self.__canvas
    
    '''
    Adiante são os métodos que rodam a aplicação
    '''

    def iniciar(self):
        
        # Clique no canvas para adicionar pontos
        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.inicio_navegacao)
        self.canvas.bind("<B1-Motion>", self.navegar)
        self.canvas.bind("<ButtonRelease-1>", self.fim_navegacao)
        self.canvas.bind("<Button-3>", self.mostrar_menu)

        self.canvas.pack()

        self.tk_root.mainloop()

    def mostrar_menu(self, evento: Event):
        menu = Menu(self.tk_root, tearoff=0)

        menu.add_command(
            label="Ponto", 
            command=lambda: self.adicionar_ponto(evento.x, evento.y)
        )

        menu.add_command(
            label="Reta", 
            command=self.comecar_reta
        )
        
        menu.add_command(
            label="Wireframe", 
            command=self.adicionar_wireframe
        )

        menu.post(evento.x_root, evento.y_root)

    def zoom(self, evento: Event):
        print("ZOOM")

    def inicio_navegacao(self, evento: Event):
        self.coords_inicio_nav = (evento.x, evento.y)
        # FIXME: Mover a viewport de forma contínua

    def navegar(self, evento: Event):
        if self.coords_inicio_nav:
            x, y = self.coords_inicio_nav

            delta_x = evento.x - x  # Movimentação horizontal
            delta_y = evento.y - y  # '' vertical
            self.coords_inicio_nav = evento.x, evento.y  # Atualizar para as próximas iterações
            
            # Move all objects by the same amount
            for obj in self.display_file.objetos:
                if isinstance(obj, Ponto):
                    obj.mover(delta_x, delta_y)
            
            # Refresh canvas
            self.refresh()

    def fim_navegacao(self, evento: Event):
        if self.coords_inicio_nav:
            self.coords_inicio_nav = None

    def adicionar_ponto(self, x, y):
        self.display_file.novo_ponto_2d(x, y)

        self.refresh()

    def comecar_reta(self):
        self.canvas.bind("<ButtonPress-1>", self.adicionar_reta)

        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<ButtonPress-3>")

        self.canvas.create_text(10, 10, anchor="nw", text="Criando reta...")

        self.escolhendo_primeiro_ponto = True
        self.escolhendo_segundo_ponto = False

        self.refresh()

    def selecionar_ponto(self, x, y):
        for obj in self.display_file.objetos:
            if isinstance(obj, Ponto):
                px, py = obj.coordenadas

                if (x - px)**2 + (y - py)**2 < 50:
                    print(f"SELECIONOU {obj.nome}")
                    self.canvas.create_text(15, 15, anchor="nw", text=f"Selecionado: {obj.nome}")
                    self.refresh()
                    return obj  

        novo_ponto = self.display_file.novo_ponto_2d(x, y)
        self.canvas.create_text(15, 15, anchor="nw", text=f"Novo ponto: {novo_ponto.nome}")
        self.refresh()
        print(f"CRIOU {novo_ponto.nome}")
        return novo_ponto

    def adicionar_reta(self, evento: Event):
        if self.escolhendo_primeiro_ponto:
            self.__ponto_inicio = self.selecionar_ponto(evento.x, evento.y)
            self.escolhendo_primeiro_ponto = False
            self.escolhendo_segundo_ponto = True 

        elif self.escolhendo_segundo_ponto:
            self.__ponto_fim = self.selecionar_ponto(evento.x, evento.y)

            if self.__ponto_inicio == self.__ponto_fim:
                self.canvas.create_text(20, 20, anchor="nw", text="Selecione outro ponto!")
                self.__ponto_fim = None
                self.refresh()

            if self.__ponto_inicio and self.__ponto_fim:
                self.display_file.nova_reta_2d([self.__ponto_inicio, self.__ponto_fim])
                nova_reta = Reta(self.__ponto_inicio, self.__ponto_fim)
                self.display_file.objetos.append(nova_reta)
                self.refresh()
                self.__adicionando_reta = False
                self.__ponto_inicio = None
                self.__ponto_fim = None

                self.canvas.unbind("<ButtonPress-1>")

                self.canvas.bind("<ButtonPress-1>", self.inicio_navegacao)
                self.canvas.bind("<B1-Motion>", self.navegar)
                self.canvas.bind("<ButtonRelease-1>", self.fim_navegacao)
                self.canvas.bind("<Button-3>", self.mostrar_menu)


    def adicionar_wireframe(self):
        print("WIREFRAM")

    def refresh(self):

        self.canvas.delete("all")

        for obj in self.display_file.objetos:
            if isinstance(obj, Ponto):
                x, y = obj.coordenadas # XXX: Essa linha só funciona em 2D
                self.canvas.create_oval(x, y, x+2, y+2, fill="black")
                self.canvas.create_text(x+1, y-7, fill="black", text=obj.nome)
            elif isinstance(obj, Reta):
                # XXX: As duas linhas abaixo só funcionam em 2D
                print(f"OBJ PONTOS: {obj.pontos}")
                p1, p2 = obj.pontos[0], obj.pontos[1]
                x1, y1 = p1.coordenadas
                x2, y2 = p2.coordenadas
                self.canvas.create_line(x1, y1, x2, y2, fill="black")

        self.canvas.pack()