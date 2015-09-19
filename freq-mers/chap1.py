import re
import itertools
fout = open('out.txt','r')
fin = open('../dataset_2994_5.txt','r')
def PatternCount(Text,Pattern):
    count = 0
    for i in xrange(len(Text)-len(Pattern)+1):
        #print Text[i:i+len(Pattern)]
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
print PatternCount('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC', 'CGCG')
def FrequentWords(Text,k):
    freqCount = []
    for i in xrange(len(Text)-k+1):
        CurPattern = Text[i:i+k]
        freqCount.append(PatternCount(Text,CurPattern))
    maxVal = max(freqCount)
    freqList = []
    for i in xrange(len(Text)-k+1):
        if freqCount[i] == maxVal:
            freqList.append(Text[i:i+k])
    return freqList


def SymbolToNumber(S):
    D = {'A':0,'C':1,'G':2,'T':3}
    return D[S]
def PatternToNumber(Pattern):
    if Pattern == '':
        return 0
    return 4*PatternToNumber(Pattern[:len(Pattern)-1]) + SymbolToNumber(Pattern[len(Pattern)-1])
def NumberToSymbol(N):
    NtoS = {0:'A',1:'C',2:'G',3:'T'}
    return NtoS[N]
def NumberToPattern(Number,k):
    if k == 1:
        return NumberToSymbol(Number)
    rem = Number % 4
    quo = Number // 4
    return NumberToPattern(quo,k-1)+NumberToSymbol(rem)

def FrequentWordsImproved(Text,k):
    freqA = [0]*((4**k))
    for i in xrange(len(Text)-k+1):
        CurPattern = Text[i:i+k]
        idx = PatternToNumber(CurPattern)
        freqA[idx] = freqA[idx]+1
    return freqA
freqA = FrequentWordsImproved('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA',3)
maxV = max(freqA)
for i in xrange(len(freqA)):
    if freqA[i] == maxV:
        print NumberToPattern(i,3)
        

#print len(set(fout.readline().split()))
