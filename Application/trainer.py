import numpy
import os

info = []

def GetTraining():
    return open('training.txt', 'r').read()

def Spew():
    print('Data content:')
    for data in info:
        print(data)

def AddWord(word : str):
    vect = numpy.array([1, 2, 3, 4, 5])
    info.append(vect)

def TrainModel():
    data = GetTraining()
    words = str.split(data, ' ')
    for word in words:
        AddWord(word)

TrainModel()
Spew()