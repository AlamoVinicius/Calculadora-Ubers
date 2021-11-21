from tkinter import *
from uber_val import *
from time import sleep
from tkinter import messagebox

class Application:
    def __init__(self, master=None):
        self.fonte = ('Arial', '10')
        self.primeiroContainer = Frame(master) 
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['padx'] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer['padx'] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack()

        self.buttonContainer = Frame(master)
        self.buttonContainer.pack()

        self.resultContainer = Frame(master)
        self.resultContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Calculadora Uber')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.tipo_combustivel = Label(self.segundoContainer, text='Tipo de combústivel:', font=self.fonte)
        self.tipo_combustivel.pack(side='left')
        self.tipo_combustivel = Entry(self.segundoContainer)
        self.tipo_combustivel['width'] = 30
        self.tipo_combustivel['font'] = self.fonte
        self.tipo_combustivel.pack(side='left')

        self.preco_combustivel = Label(self.terceiroContainer, text =f'Preço do combustível selecionado:', font=self.fonte)
        self.preco_combustivel.pack(side='left')
        self.preco_combustivel = Entry(self.terceiroContainer)
        self.preco_combustivel['width'] = 7
        self.preco_combustivel['font'] = self.fonte
        self.preco_combustivel.pack(side='left')

        self.autonomia = Label(self.quartoContainer, text='Autonomia do carro c/ combustivel selecionado:', font=self.fonte)
        self.autonomia.pack(side='left')
        self.autonomia = Entry(self.quartoContainer)
        self.autonomia['width'] = 7
        self.autonomia.pack(side='left')
        
        self.valor = Label(self.quintoContainer, text='Valor total da CORRIDA ou DIA:', font=self.fonte)
        self.valor.pack(side='left')
        self.valor = Entry(self.quintoContainer)
        self.valor['width'] = 7
        self.valor.pack()

        
        self.quilometragem = Label(self.sextoContainer, text='Quilometragem total percorrida no DIA ou CORRIDA:', font=self.fonte)
        self.quilometragem.pack(side='left')
        self.quilometragem = Entry(self.sextoContainer)
        self.quilometragem['width'] = 7
        self.quilometragem.pack()

        self.lb = Label(self.resultContainer, text='', borderwidth=1, relief='solid')
        self.lb.pack()        
        def bt_click():
            try:
                preco_comb = float(self.preco_combustivel.get())
                autonomia = float(self.autonomia.get())
                valor_total = float(self.valor.get())
                km = float(self.quilometragem.get())
                res = calculo_total(preco_comb, autonomia, valor_total, km)
            except:
                messagebox.showerror('ERROR', 'Valores inválidos\nFormato ex.: 9.99')
            if self.lb['text'] == '':
                sleep(1)
                self.lb['text'] = F'Resultados para "{self.tipo_combustivel.get()}"\n{minha_tabela(res)}'
                self.lb.pack()
                self.bt['text'] = 'LIMPAR'
            else:
                self.bt['text'] = 'RESULTADO'
                self.lb['text'] = ''
            

        self.bt = Button(self.buttonContainer, text='RESULTADO', width=20, command=bt_click)
        self.bt.pack()

        

janela = Tk()
janela.title('Calculator Uber')
Application(janela)
janela.mainloop()
