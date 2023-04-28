import customtkinter
from anytree import Node
from anytree.exporter import DotExporter
import subprocess

customtkinter.set_appearance_mode("System")

grammar = {'S': ['E'], 'E': ['T + E', 'T'], 'T': ['int', '( E )']}

def parse(input_string):
    tokens = input_string.split()  
    lookahead = tokens.pop(0)      
    parse_S()                      
    if lookahead != '$':
        raise SyntaxError('Unexpected token: {}'.format(lookahead))
    
def parse_S():
    parse_E()

def parse_E():
    parse_T()
    if lookahead == '+':
        match('+')
        parse_E()

def parse_T():
    if lookahead == 'int':
        match('int')
    elif lookahead == '(':
        match('(')
        parse_E()
        match(')')

def match(expected):
    global lookahead
    if lookahead == expected:
        lookahead = expected.pop(0)
    else:
        raise SyntaxError('Unexpected token: {}'.format(lookahead))

def analizar(cadena):
    return 1

def generar_arbol(lista):
    nodo_raiz = Node(lista[0])
    if len(lista) > 1:
        for hijo in lista[1:]:
            nodo_hijo = generar_arbol(hijo)
            nodo_hijo.parent = nodo_raiz
    return nodo_raiz

class App(customtkinter.CTk):
    def __init__(self):
# ------------------------------------------------------------------------------------------------------
# No le muevas si no le sabes
# ------------------------------------------------------------------------------------------------------
        super().__init__()
        self.geometry("220x240")
        self.title("ADR")
        self.mainInput = customtkinter.CTkEntry(self, placeholder_text="Ingrese la cadena")
        self.mainInput.grid(row=0, column=2, padx=40, pady=25)
        self.button = customtkinter.CTkButton(self, command=self.button_click1, text="Checar cadena")
        self.button.grid(row=1, column=2, padx=40, pady=10)
        self.button2 = customtkinter.CTkButton(self, command=self.button_click2, text="Generar arbol")
        self.button2.grid(row=3, column=2, padx=40, pady=10)
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=4, column=2, padx=40, pady=10)
# ------------------------------------------------------------------------------------------------------

    def button_click1(self):
        cadena = self.mainInput.get().lower()
        if cadena == "" :
            self.label.configure(text="Ingresa una cadena")
            return
        else:
            if analizar(cadena) == 1 :
                texto = "La cadena es aceptada."
            elif analizar(cadena) == 0:
                texto = "La cadena no es aceptada."
            self.label.configure(text = texto)

    def button_click2(self):
        self.label.configure(text="Arbol generado")
        arbol = generar_arbol(['A', ['B', ['X'], ['W']], ['C', ['F'], ['G']]]) # Como chingados metemos cosas
        DotExporter(arbol).to_dotfile("arbol.dot")
        comando = "dot -Tpng arbol.dot -o arbol.png"
        comando2 = "rm arbol.png"
        subprocess.run(comando2, shell=True, capture_output=True, text=True)
        subprocess.run(comando)

app = App()
app.mainloop()