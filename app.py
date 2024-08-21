
import tkinter as tk
from tkinter import ttk, font,messagebox
from tkinter import photoimage



janela = tk.tk()
janela.tilte("app de tarefas")
janela.configure(bg="FOFOFO")
janela.geometry("500x600")


frame_em_ediçao = none 

def adicionar_tarefa(): 
      global frame_em_ediçao 
      tarefa = entrada_tarefa.get().strip()
      if tarefa and tarefa != "escreva sua tarefa aqui: ":
            if frame_em_ediçao is not none:
                  atualizar_tarefa(tarefa)
                  frame_em_ediçao = none 
            else: 
                  adicionar_item_tarefa(tarefa)         
                  entrada_tarefa.delete(0,  tk.END)  

      else:
            messagebox.showwarning("Entrada ivalida", "por favor insira uma tarefa valida.")  

def adicionar_item_terefa(terefa):      
    frame_terefa = tk.frame(canvas_interior, bg="white", bd=1,relief=tk.SOLID)

    label_tarefa =tk.label(frame_terefa, texte=terefa, font =("Garamond", 16), bg="white", width =25, height=2, achor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.x,padx=10, pady=5)

    botao_editar = tk.button(frame_terefa, image=icon_editar, command=lambda f=frame_tarefa,l=label_tarefa:preparar_edicao(f, l), bg="while", relief=tk.FLAT)
    botao_editar.pack(side=tk.RICK,padx=5)
    
    botao_deletar = tk.button(frame_tarefa, image=icon_excluir, command=lambda f=frame_tarefa: deletar_terefa(f), bg="while", relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.x padx=5, pady=5)


    











