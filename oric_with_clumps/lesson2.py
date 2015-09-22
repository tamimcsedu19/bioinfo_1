import re
import chap1
import time
fout = open('out.txt','w')
fin = open('../E-coli.txt','r')
def revComplement(Pat):
    D = {'A':'T','G':'C','T':'A','C':'G'}
    rev = ''
    for c in Pat:
        rev+=D[c]
    return rev[::-1]
print revComplement('GCTAGCT')
def matchPattern(Text,Pat):
    return [m.start() for m in re.finditer('(?='+Pat+')', Text)]

def clumpFormingKmerFinding(Genome,k,L,t):
    res = set()
    freqA = chap1.FrequentWordsImproved(Genome[:L],k)
    qNToPat = []
    qPatToN = {}
    for i in xrange(4**k):
        Pat = chap1.NumberToPattern(i,k)
        qNToPat.append(Pat)
        qPatToN[Pat] = i
    print 'start'
    timestart = time.clock()
    for i in xrange(len(freqA)):
        if freqA[i] >= t:
            res.add(qNToPat[i])
    for i in xrange(1,len(Genome)-L):
        leavingPattern = Genome[i-1:i-1+k]
        enteringPattern = Genome[i+L-k:i+L]
        nLeavingPattern = qPatToN[leavingPattern]
        nEnteringPattern = qPatToN[enteringPattern]
        freqA[nLeavingPattern] = freqA[nLeavingPattern]-1
        freqA[nEnteringPattern] = freqA[nEnteringPattern]+1
        if freqA[nEnteringPattern] >= t:
            res.add(enteringPattern)
    timeend = time.clock()
    print timeend-timestart
    return res

Genome = fin.readline().strip()
#args = fin.readline().split()
print(len(Genome))
clumpsFormingKmer =  clumpFormingKmerFinding(Genome,9,500,3)

distinct = list(set(clumpsFormingKmer))
    #fout.write(s+' ')
print len(distinct)
