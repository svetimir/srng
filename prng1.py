# pseudorandom number generator
# генератор псевдослучайных чисел
# по линейному конгруэнтному методу
# программа выводит в стандартный вывод
# указанное количество псевдослучайных чисел
# в csv-формате 

# Georgy Yashin, ifi@yandex.ru
# 27.08.2017

import math
import time
import sys

rmax=1e6
aboutru="ИСПОЛЬЗОВАНИЕ: python prng1.py <N> \nгенератор псевдослучайных чисел по линейному конгруэнтному методу \nпрограмма выводит в стандартный вывод \nуказанное количество (N) псевдослучайных чисел от 0 до 32767 в csv-формате\n"
about="USAGE: python prng1.py <N> \nSimple congruential random number generator utility, \ngenerates given amount (N) of random numbers from 0 to 32767 \nand outputs them to STDOUT in CSV format"

if __name__=="__main__":
    if len(sys.argv)>1:
        if sys.argv[1]=="-help":
            print(about)
            exit(0)
        try:
            sz=int(sys.argv[1])
            if sz>rmax: raise ValueError
        except:
            print('Введите корректное число\nВведите python prng1.py -help для вывода справки')
            exit(1)            
    else:
        print(about)
        exit(1)

m=32768
a=23
b=12345

def prng(seed,size):
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return ','.join([str(a) for a in r[1:size]])

t=time.time()
print(prng(t,sz))
exit(0)
