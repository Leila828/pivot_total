from __future__ import division
from Tkinter import *
from Tkinter import Entry
import numpy as np


def max(M, p):
    # rech max
    list = []
    # imax=0
    # jmax=0
    pmax = 0
    for i in range(p, len(M)):
        for j in range(p, len(M[0])):
            if abs(M[i][j]) > abs(pmax):
                pmax = M[i][j]
                imax = i
                jmax = j
    list.append(imax)
    list.append(jmax)
    return list


def ligne(p, M, imax):
    for i1 in range(p, len(M) + 1):
        tmp = M[imax][i1]
        M[imax][i1] = M[p][i1]
        M[p][i1] = tmp
    return M


def colonne(p, M, jmax):
    for j1 in range(p, len(M)):
        prm = M[j1][jmax]
        M[j1][jmax] = M[j1][p]
        M[j1][p] = prm
    return M


def new(M, b, bol):
    if bol == False:
        lis = list(M)
        for i in range(len(b)):
            lis[i].append(b[i])

        return lis


def elimination(m, p):
    for z in range(p + 1):
        print(m[z])
    for i2 in range(p + 1, len(m)):

        n = (m[i2][p] / m[p][p])

        for j2 in range(len(m[0])):
            k = (m[i2][j2] - (n * m[p][j2]))

            m[i2][j2] = k
        print(m[i2])

def repondre():

 v = False
 m=np.array(eval(reponse.get()))
 m2=np.array(eval(reponse2.get()))

 x=np.linalg.solve(m, m2)

 affichage['text'] = x






Fenetre= Tk()
Fenetre.title('Mon nom')
nom = Label(Fenetre, text = 'Votre matrice :')
reponse = Entry(Fenetre)  # type: Entry
reponse2 = Entry(Fenetre)

valeur2 = Button(Fenetre, text =' ok', command=repondre)
affichage = Label(Fenetre, width=10)

nom.pack()

reponse.pack()
reponse2.pack()
valeur2.pack()
affichage.pack()

Fenetre.mainloop()
