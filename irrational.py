from math import pi
import random, winsound

rawFreqs = """  C4    261.63 	131.87
                C#4/Db4  	277.18 	124.47
                D4	293.66 	117.48
                D#4/Eb4  	311.13 	110.89
                E4	329.63 	104.66
                F4	349.23 	98.79
                F#4/Gb4  	369.99 	93.24
                G4	392.00 	88.01
                G#4/Ab4  	415.30 	83.07
                A4	440.00 	78.41
                A#4/Bb4  	466.16 	74.01
                B4	493.88 	69.85
                C5	523.25 	65.93
                C#5/Db5  	554.37 	62.23
                D5	587.33 	58.74
                D#5/Eb5  	622.25 	55.44
                E5	659.25 	52.33"""
                
durations = [250, 500, 1000, 2000]
                
def majorIntervals(n):
    return [n, n+2, n+4, n+5, n+7, n+9, n+11, n+12, n+14, n+16]

allFreqs = map(float, rawFreqs.split()[1::3])
majorFreqs = [ int(allFreqs[i]) for i in majorIntervals(0) ]
freqDict = dict(zip(range(10), majorFreqs))

piList = list(str(pi))
del piList[1]
for digit in piList:
    winsound.Beep(freqDict[int(digit)], random.choice(durations))