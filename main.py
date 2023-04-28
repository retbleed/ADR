import customtkinter
from anytree import Node
from anytree.exporter import DotExporter
import subprocess

customtkinter.set_appearance_mode("System")

def analizar(cadena):
    global pos
    pos = 0
    if A(cadena):
        if pos == len(cadena):
            return True
    return False

def A(cadena):
    global pos
    if cadena[pos] == 'a':
        pos += 1
        if B(cadena) and C(cadena):
            return True
    return False

def B(cadena):
    global pos
    if cadena[pos] == 'b':
        pos += 1
        return True
    return False

def C(cadena):
    global pos
    if cadena[pos] == 'c':
        pos += 1
        return True
    return False

def generar_arbol(lista):
    nodo_raiz = Node(lista[0])
    if len(lista) > 1:
        for hijo in lista[1:]:
            nodo_hijo = generar_arbol(hijo)
            nodo_hijo.parent = nodo_raiz
    return nodo_raiz

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Analizador Sintactico")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click, text="Generar arbol")
        self.button.grid(row=1, column=2, padx=230, pady=10)

        self.mainInput = customtkinter.CTkEntry(self, placeholder_text="Ingrese la cadena")
        self.mainInput.grid(row=0, column=2, padx=230, pady=25)

    # add methods to app
    def button_click(self):
        cadena = self.mainInput.get()
        print(analizar(cadena))
        arbol = generar_arbol(['A', ['B', ['D'], ['E']], ['C', ['F'], ['G']]])
        DotExporter(arbol).to_dotfile("arbol.dot")
        comando = "dot -Tpng arbol.dot -o arbol.png"
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

app = App()
app.mainloop()