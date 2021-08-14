{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Dcictionary in python\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4: 8, 'str': 2}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {}\n",
    "d[4] = 3\n",
    "d['str'] = 8\n",
    "\n",
    "c = {4:8 ,'str':2}\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'str': 8}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del d[4]\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "dict_keys([21])\n",
      "dict_values([2])\n"
     ]
    }
   ],
   "source": [
    "d1 ={21:2}\n",
    "d2 ={43:4}\n",
    "print(d1==d2)\n",
    "print(d1.keys())\n",
    "print(d1.values())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      " not a prime number\n"
     ]
    }
   ],
   "source": [
    "#conditios\n",
    "#to find prime number\n",
    "n = int(input())\n",
    "prime = True\n",
    "for i in range(2,n):\n",
    "    if(n%i) == 0:\n",
    "        prime = False;\n",
    "        break;\n",
    "            \n",
    "if prime == False:\n",
    "    print(\" not a prime number\")\n",
    "else:\n",
    "    print(\"is prime\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# functions in python\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sum(a, b):\n",
    "    return a+b\n",
    "z = sum(4,5)\n",
    "z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def power(x,y =5):\n",
    "    return x**y\n",
    "p = power(2)\n",
    "p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#name and positions association\n",
    "def sum1(a=1, b=2, c=3):\n",
    "    return a+b+c\n",
    "d = sum1(5, c=5,b=8)\n",
    "d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2D lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0],\n",
       " [0, 0, 0]]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D = [[0,0,0] for i in range(10)]\n",
    "D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
