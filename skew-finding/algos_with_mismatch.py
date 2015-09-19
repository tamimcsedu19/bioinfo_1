import sys
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


def hamming_distance(T1,T2):
    cnt = 0
    for c1,c2 in zip(T1,T2):
        if c1 != c2:
            cnt = cnt+1
    return cnt

def ApproxPatternPos(Pattern,Text,d):
    start_pos = []
    for i in range(len(Text)-len(Pattern)+1):
        print hamming_distance(Text[i:i+len(Pattern)],Pattern)
        if hamming_distance(Text[i:i+len(Pattern)],Pattern) <= d:
            start_pos.append(i)
    return start_pos
def ApproxPatternCount(Pattern,Text,d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        #print Text[i:i+len(Pattern)]
        if hamming_distance(Text[i:i+len(Pattern)],Pattern) <= d:
            count = count+1
    return count

def d_neighbourHood(Pat,d):
    if d == 0:
        return [Pat];
    if len(Pat) == 1:
        return ['A','G','C','T']
    Neighbours = []
    SuffixNeighbours = d_neighbourHood(Pat[1:],d)
    for s_neighbour in SuffixNeighbours:
        if hamming_distance(s_neighbour,Pat[1:]) < d:
            Neighbours.append('A'+s_neighbour)
            Neighbours.append('C'+s_neighbour)
            Neighbours.append('G'+s_neighbour)
            Neighbours.append('T'+s_neighbour)
        else:
            Neighbours.append(Pat[0]+s_neighbour)
    return Neighbours

def freq_words_mistmatch(Text,k,d):
            
    freqA = [0]*((4**k))
        
    for i in range(0,len(Text)-k+1):
        neighbours = d_neighbourHood(Text[i:i+k],d);
        for neighbour in neighbours:
            pos = PatternToNumber(neighbour)
            freqA[pos] = freqA[pos] + 1
    
    max_freq = max(freqA)
    
    res = set()
    for i in range(0,4**k):
        if freqA[i] == max_freq:
            res.add(NumberToPattern(i,k))
    return res    
def revComplement(Pat):
    D = {'A':'T','G':'C','T':'A','C':'G'}
    rev = ''
    for c in Pat:
        rev+=D[c]
    return rev[::-1]
def freq_words_mistmatch_with_reverse(Text,k,d):
     
            
    freqA = [0]*((4**k))
    freqAR = [0]*((4**k))
        
    
    
    for i in range(0,len(Text)-k+1):
        neighbours = d_neighbourHood(Text[i:i+k],d);
        for neighbour in neighbours:
            pos1 = PatternToNumber(neighbour)
            pos2 = PatternToNumber(revComplement(neighbour))
            freqA[pos1] = freqA[pos1] + 1
            freqAR[pos2] = freqAR[pos2] + 1
    
    freq = [0]*((4**k))
    for i in range(0,4**k):
        freq[i] = freqA[i]+freqAR[i]
        
    
    max_freq = max(freq)
    
    res = set()
    for i in range(0,4**k):
        '''
        print NumberToPattern(i,k)+':',
        print freqA[i],
        print freqAR[i]
        '''
        if freq[i] == max_freq:
            res.add(NumberToPattern(i,k))
    return res    


print len(d_neighbourHood('ACGT',3))



'''

f_in = open('in.txt','r')
f_out = open('out.txt','w')
#Pat = f_in.readline().strip()

Text = f_in.readline().strip()
kd = f_in.readline().strip().split()
k = int(kd[0])
d = int(kd[1])
res = freq_words_mistmatch_with_reverse(Text,k,d)
#f_out.write(str(res))

for i in res:
    f_out.write(i)
    f_out.write(' ')
    
'''

