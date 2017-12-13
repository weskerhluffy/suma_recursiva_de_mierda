'''
Created on 12/12/2017

@author: 

XXX: https://www.hackerrank.com/challenges/recursive-digit-sum/problem
'''

import logging
import sys

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None



# XXX: https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
def entero_a_lista(n):
    return [int(x) for x in str(n)]

def superDigit(n, k):
    caca=sum(map(int,n))%9
    if not caca:
        caca=9
    caca*=k
    caca=sum(entero_a_lista(caca))%9
    if not caca:
        caca=9
    return caca

if __name__ == "__main__":
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = superDigit(n, k)
    print(result)
