from tkinter import *
import tkinter
from tkinter import font

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#1fff0a"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul


janela = Tk()
janela.title(' ')
janela.geometry('400x200')
janela.config(bg=cor1)
janela.resizable(width=False,height=False)



#Def Variaveis Globais

global tempo
global rodar
global contador
global limitador
limitador = 59

tempo = "00:00:00"
rodar = False
contador = -3

def iniciar():
    global tempo
    global contador
    global limitador


    if rodar:
        #contagem regressiva
        if contador <=-1:
            inicio = 'Começando em ' +str(-contador) 
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 20'
            
        #Rodando Cronometro
        else:
            label_tempo['font'] = 'Times 46 bold'
            temporaria = str(tempo)
            h,m,s = map(int,temporaria.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)
        
            if(s>=limitador):
                contador = 0
                m+=1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)



            #Atualizando valores
            temporaria = str(h[-2:])+':' +str(m[-2:])+':'+str(s[-2:])
            label_tempo['text'] = temporaria 

            tempo = temporaria


        contador += 1
        label_tempo.after(1000, iniciar)
        
def start():
    global rodar
    rodar = True
    botao_iniciar['state'] = DISABLED
    iniciar()   

def pause():
    global rodar
    rodar = False
    botao_iniciar['state'] = NORMAL

def restart():
    global tempo
    global contador

    #reiniciando o contador
    contador = 0

    #reiniciando o tempo 
    tempo = "00:00:00"
    label_tempo['text'] = tempo
    botao_iniciar['state'] = DISABLED

#Labels-------------

label_app = Label(janela, text='Cronômetro',font='Arial 12',bg=cor1,fg=cor2,)
label_app.place(x=20,y=5)

label_tempo = Label(janela, text=tempo,font='times 46 bold',bg=cor1,fg=cor3,)
label_tempo.place(x=90,y=50)

#Botoes

botao_iniciar = Button(janela,command=start,text='Iniciar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 10 bold', relief='raised',overrelief='ridge')
botao_iniciar.place(x=50 ,y=150)

botao_pausar = Button(janela,command=pause,text='Pausar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 10 bold', relief='raised',overrelief='ridge')
botao_pausar.place(x=150 ,y=150)

botao_reiniciar = Button(janela,command=restart ,text='Reiniciar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 10 bold', relief='raised',overrelief='ridge')
botao_reiniciar.place(x=250 ,y=150)








janela.mainloop()