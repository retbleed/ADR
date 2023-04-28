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
        # No le muevas si no le sabes
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

    def button_click1(self):
        cadena = self.mainInput.get()
        if cadena == "" :
            self.label.configure(text="Ingresa una cadena")
            return
        else:
            if analizar(cadena.lower()) == 1 :
                texto = "La cadena es aceptada."
            elif analizar(cadena.lower()) == 0:
                texto = "La cadena no es aceptada."
            self.label.configure(text = texto)

    def button_click2(self):
        self.label.configure(text="Arbol generado")
        arbol = generar_arbol(['A', ['B', ['D'], ['E']], ['C', ['F'], ['G']]]) # Como chingados metemos cosas
        DotExporter(arbol).to_dotfile("arbol.dot")
        comando = "dot -Tpng arbol.dot -o arbol.png"
        subprocess.run(comando, shell=True, capture_output=True, text=True)

app = App()
app.mainloop()