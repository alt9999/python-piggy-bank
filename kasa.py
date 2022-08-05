from prettytable import PrettyTable
import sys
from datetime import datetime
tabela = PrettyTable(['Data', 'Zostało (PLN)', 'Uzbierano (PLN)'])
cena = 1000
t = []

try: 
    if(sys.argv[1] != ''):
        with open('kasa.txt', 'a') as f:
            if(int(sys.argv[1]) > 0):
                f.write(datetime.today().strftime('%Y:%m:%d') + "|" + sys.argv[1] + "\n")
            elif(int(sys.argv[1]) < 0):
                f.write(datetime.today().strftime('%Y:%m:%d') + "|" + sys.argv[1] + "\n")
except:
    pass
with open('kasa.txt') as f:
    kasa = f.read().split()
    for y in kasa:
        t.append(y.split('|')[1])
        tabela.add_row([y.split('|')[0], cena - sum(list(map(int, t))), y.split('|')[1]])
    tabela.add_row(['', '',f"Suma: {sum(list(map(int, t)))}"])
    print(tabela)
            
       
        

        

        

    


