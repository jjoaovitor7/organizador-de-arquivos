#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import logging


def main(self):
    def setTitle():
        self.title('Organizador de Arquivos')


    def setGeometry():
        self.geometry('450x165')


    def colorWindow():
            self.config(bg='#222')

    style = ttk.Style()
    style.configure('main.TLabel', background='#222',
                    foreground='#fff', font=('Times New Roman', 14))
    style.configure('main.TButton', background='#222',
                    foreground='#000', font=('Times New Roman', 14),
                    width=11, relief=tk.RAISED)

    formatos={
        "imagem": {"formatos": "*.bmp *.jfif *.jpeg *.jpg *.nef *.png *.raw *.svg *.tiff *.webp *.gif"},
        "video": {"formatos": "*.avi *.mp4 *.mpg *.webm"},
        "documento": {"formatos": "*.doc *.docx *.odt *.pdf"},
        "musica": {"formatos": "*.aac *.mp3 *.ogg *.wav"}
     }

    def imagesMov():
        os.system('mkdir Imagens')
        logging.basicConfig(filename='info.log', format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.INFO)
        logging.info('Imagens Movidas')
        os.system('mv -v ' + formatos["imagem"]["formatos"] + ' Imagens >> info.log')


    def videosMov():
        os.system('mkdir Vídeos')
        logging.basicConfig(filename='info.log', format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.INFO)
        logging.info('Vídeos Movidos')
        os.system('mv -v ' + formatos["video"]["formatos"] + ' Vídeos >> info.log')


    def docsMov():
        os.system('mkdir Documentos')
        logging.basicConfig(filename='info.log', format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.INFO)
        logging.info('Documentos Movidos')
        os.system('mv -v ' + formatos["documento"]["formatos"] + ' Documentos >> info.log')


    def musicsMov():
        os.system('mkdir Músicas')
        logging.basicConfig(filename='info.log', format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.INFO)
        logging.info('Músicas Movidas')
        os.system('mv -v ' + formatos["musica"]["formatos"] + ' Músicas >> info.log')


    def setWidgets():
        titleLabel = ttk.Label(self, text='Organizador de Arquivos',
                               style='main.TLabel').pack(side=tk.TOP)

        actualFolderLabel = ttk.Label(self, text=os.getcwd(),
                              style='main.TLabel')
        actualFolderLabel.pack(side=tk.TOP)

        imagesButton = ttk.Button(self, text='Imagens', style='main.TButton',
                                  command=imagesMov).pack(side=tk.TOP)
        videosButton = ttk.Button(self, text='Videos', style='main.TButton',
                                  command=videosMov).pack(side=tk.TOP)
        docsButton = ttk.Button(self, text='Documentos', style='main.TButton',
                                command=docsMov).pack(side=tk.TOP)
        musicsButton = ttk.Button(self, text='Músicas', style='main.TButton',
                                  command=musicsMov).pack(side=tk.TOP)

        def changeFolder(event):
            try:
                folder = filedialog.askdirectory(initialdir=os.getcwd(), title='Selecionar Pasta')
                os.chdir(folder)
                actualFolderLabel.config(text=os.getcwd())
            except FileNotFoundError:
                logging.basicConfig(filename='info.log',
                                    format='[%(asctime)s] %(levelname)s: %(message)s',
                                    level=logging.INFO)
                logging.info('A pasta não foi encontrada!')
        actualFolderLabel.bind('<Button-1>', changeFolder)

    setTitle()
    setGeometry()
    colorWindow()

    setWidgets()


def run():
    root = tk.Tk()
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
