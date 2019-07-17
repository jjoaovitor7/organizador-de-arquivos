#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import os


def main(self):
    self.title('Organizador de Arquivos')
    self.config(bg='#5c646e')
    self.geometry('300x150')

    style = ttk.Style()
    style.configure('main.TLabel', background='#5c646e',
                    foreground='#000000', font=('Times New Roman', 14))
    style.configure('main.TButton', background='#727c87',
                    foreground='#000000', font=('Times New Roman', 14),
                    width=11, relief=tk.RAISED)

    l_titulo = ttk.Label(self, text='Organizador de Arquivos',
                         style='main.TLabel')

    def mover_imagens():
        os.system('mkdir Imagens')
        os.system('mv *.jpg *.png Imagens')

    def mover_videos():
        os.system('mkdir Vídeos')
        os.system('mv *.avi *.mp4 Vídeos')

    def mover_documentos():
        os.system('mkdir Documentos')
        os.system('mv *.doc *.docx *.odt Documentos')

    def mover_musicas():
        os.system('mkdir Músicas')
        os.system('mv *.mp3 Músicas')

    b_imagens = ttk.Button(self, text='Imagens', style='main.TButton',
                           command=mover_imagens)
    b_videos = ttk.Button(self, text='Videos', style='main.TButton',
                          command=mover_videos)
    b_documentos = ttk.Button(self, text='Documentos', style='main.TButton',
                              command=mover_documentos)
    b_musicas = ttk.Button(self, text='Músicas', style='main.TButton',
                           command=mover_musicas)

    l_titulo.pack(side=tk.TOP)

    b_imagens.pack(side=tk.TOP)
    b_videos.pack(side=tk.TOP)
    b_documentos.pack(side=tk.TOP)
    b_musicas.pack(side=tk.TOP)


def run():
    root = tk.Tk()
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
