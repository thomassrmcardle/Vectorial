import numpy
import random

info = []

def GetTraining():
    try:
        return open('training.txt', 'r').read()
    except FileNotFoundError:
        print("Error: training.txt file not found in the current directory.")
        return ""

def Spew():
    print('Data content:')
    for data in info:
        print(data)

def RandomCord():
    return random.randint(-100, 100)

def CheckWord(word : str):
    for point in info:
        if point[0] == word:
            return True
    return False

def AddWord(word : str):
    if (CheckWord(word)): return
    vect = numpy.array([RandomCord(), RandomCord(), RandomCord(), RandomCord(), RandomCord()])
    info.append([word, vect])

def ApplyWord(word : str, change):
    print("Updated")

def GetWord(word : str):
    for point in info:
        if point[0] == word:
            return point[1]

def ApplyWeight(VectA, VectB, weight : float):
    return (VectA*weight + VectB*(1-weight))

def Attract(wordA : str, wordB : str, weight : float):
    pointA = GetWord(wordA)
    pointB = GetWord(wordB)
    avg = (pointA+pointB)/2
    
    newA = ApplyWeight(pointA, avg, weight)
    newB = ApplyWeight(pointA, avg, weight)

    ApplyWord(wordA, newA)
    ApplyWord(wordB, newB)

def TrainModel():
    data = GetTraining().lower()
    words = str.split(data, ' ')
    for word in words:
        AddWord(word)
    
    for sentence in data.split('\n'):
        innerWords = sentence.split(' ')
        for wordX in innerWords:
            for wordY in innerWords:
                Attract(wordX, wordY, 0.5)
            


TrainModel()
Spew()