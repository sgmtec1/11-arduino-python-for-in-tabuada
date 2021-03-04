# Programa Tabuada em Python
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')
print('TABUADA DO NUM: ')
tabuada = int(input(lcd.escrever(board, 0, 0, 'TABUADA DO NUM: ')))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
    lcd.escrever(board, 0, 0, 'TABUADA SGMTEC1 ')
    lcd.escrever(board, 0, 1, "%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
    time.sleep(2.0)
lcd.escrever(board, 0, 1, 'FIM             ')
lcd.limpar(board)
board.exit()