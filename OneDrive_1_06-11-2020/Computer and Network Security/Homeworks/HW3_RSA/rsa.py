# -*- coding: utf-8 -*-
"""RSA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jk6NKZmJcMwrcD__No8jCyCOy4uTio_B

##RSA Implementation #Homework3
"""

import random
import sympy
import timeit
from Crypto.Util.number import bytes_to_long, long_to_bytes

def randchoose():
	fo = open('primes-to-1000k.txt', 'r')
	lines = fo.read().splitlines()
	fo.close()
	p = int(lines[random.randint(100, 300)])
	q = int(lines[random.randint(100, 300)])
	print("p: ",p)
	print("q: ",q)
	return p, q

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

def pubKey():
  p, q = randchoose()
  n = int(p)*int(q)
  phi = (p-1)*(q-1)
  while(1):
    e = random.choice(range(1, phi-1))
    if(gcd(e,phi)) == 1:
      break
  return (n, e, phi)

def encrypt(x, n, e):
  y = pow(x,e,n)
  return y

def main():
	start = timeit.timeit()
	n, e, phi = pubKey()
	print("n: ",n)
	print("e: ",e)
	print("phi: ",phi)
	x = 'Done.'
	print("Plaintext: ",x)
	x = bytes_to_long(x.encode('utf-8'))
	y = encrypt(x, n, e)
	print("Ciphertext: ", y)
	end = timeit.timeit()
	print("time to encrypt: ", end-start)
	start = timeit.timeit()
	d = sympy.mod_inverse(e, phi)
	print(" ")
	print("d: ",d)
	x = encrypt(y, n, d)
	x = long_to_bytes(x)
	print("Decrypted text: ",x)
	end = timeit.timeit()
	print("time to encrypt: ", end-start)

main()