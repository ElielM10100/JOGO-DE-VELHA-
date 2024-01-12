import tkinter as tk
from tkinter import messagebox

class JogoDaVelhaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.jogadores = ["X", "O"]
        self.vez_do_jogador = 0

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                                              command=lambda linha=i, coluna=j: self.celula_clicada(linha, coluna))
                self.botoes[i][j].grid(row=i, column=j)

    def celula_clicada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogadores[self.vez_do_jogador]
            self.botoes[linha][coluna].config(text=self.jogadores[self.vez_do_jogador], state=tk.DISABLED)

            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Parabéns, Jogador {self.jogadores[self.vez_do_jogador]}! Você venceu!")
                self.resetar_jogo()
            elif all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.resetar_jogo()
            else:
                self.vez_do_jogador = 1 - self.vez_do_jogador  # Alternar entre jogadores

    def verificar_vitoria(self):
        # Verificar linhas e colunas
        for i in range(3):
            if all([self.tabuleiro[i][j] == self.jogadores[self.vez_do_jogador] for j in range(3)]) or all([self.tabuleiro[j][i] == self.jogadores[self.vez_do_jogador] for j in range(3)]):
                return True

        # Verificar diagonais
        if all([self.tabuleiro[i][i] == self.jogadores[self.vez_do_jogador] for i in range(3)]) or all([self.tabuleiro[i][2 - i] == self.jogadores[self.vez_do_jogador] for i in range(3)]):
            return True

        return False

    def resetar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = " "
                self.botoes[i][j].config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_velha_gui = JogoDaVelhaGUI(root)
    root.mainloop()
