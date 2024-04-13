import tkinter as tk
from bot_app.gui.interfaz import InterfazContador

def main():
    root = tk.Tk()
    app = InterfazContador(root)
    root.mainloop()

if __name__ == "__main__":
    main()
