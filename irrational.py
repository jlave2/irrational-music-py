from math import pi
import random, winsound

#-------------------------------------------------------------------------------
# Read frequency data from the provided text file and store each tone as a list
# row. The frequency value is converted to an int while storing.
#-------------------------------------------------------------------------------
allFreqs = []
freqFile = open('freqs.txt', 'r')
for line in freqFile:
    allFreqs.append([ line.split()[0], int(line.split()[1]) ])
freqFile.close()

#-------------------------------------------------------------------------------
# Convert pi into a list of ints, removing the decimal point.
#-------------------------------------------------------------------------------
piList = list(str(pi))
del piList[1]
piList = [int(digit) for digit in piList]

#-------------------------------------------------------------------------------
# Define beep durations in milliseconds.
#-------------------------------------------------------------------------------
durations = [250, 500, 1000, 2000]

def majorIntervals(n):
    return [n, n+2, n+4, n+5, n+7, n+9, n+11, n+12, n+14, n+16]
    
def minorIntervals(n):
    return [n, n+2, n+3, n+5, n+7, n+8, n+10, n+12, n+14, n+15]    

def getParams():
    global key, octave, scale
    key = input('Choose a key (use # or b): ')
    octave = input('Choose an octave (0-8): ')
    scale = input('Choose a scale (maj/min): ')

def playMusic():
    getParams()
    if scale == 'maj':
        toneInds = majorIntervals([allFreqs.index(i) for i in allFreqs \
                   if key + octave in i[0]][0])
    if scale == 'min':
        toneInds = minorIntervals([allFreqs.index(i) for i in allFreqs \
                   if key + octave in i[0]][0])
    else:
        print('Invalid scale. Try again.')
        playMusic()
    if max(toneInds) > len(allFreqs):
        print('I\'ve run out of tones. Choose a lower octave.')
        playMusic()
    else:
        print('Playing...')
        freqDict = dict(zip(range(10), toneInds)) 
        for digit in piList:
            randDur = random.choice(durations)
            print('...' + allFreqs[freqDict[digit]][0] + ' (digit ' + \
                   str(digit) + ') for ' + str(randDur/1000) + ' s')
            winsound.Beep(allFreqs[freqDict[digit]][1], randDur)
            
playMusic()

'''
allFreqs = map(float, rawFreqs.split()[1::3])
majorFreqs = [ int(allFreqs[i]) for i in majorIntervals(0) ]
freqDict = dict(zip(range(10), majorFreqs))

piList = list(str(pi))
del piList[1]
for digit in piList:
    winsound.Beep(freqDict[int(digit)], random.choice(durations))
    '''