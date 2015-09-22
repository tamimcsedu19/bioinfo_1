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

def DistanceBetweenPatternAndStrings(DNAs,Pattern):
    k = len(Pattern)
    d = 0
    for Text in DNAs:
        hamming_dist = float('inf')
        for i in xrange(0,len(Text)-k+1):
            cdist = hamming_distance(Text[i:i+k],Pattern)
            if( cdist < hamming_dist):
                hamming_dist = cdist
    
        d = d+hamming_dist
    return d
    
def MedianString(DNAs,k):
    min_score = float('inf')
    for i in xrange(4**k):
        cPat = NumberToPattern(i,k)
        cDist = DistanceBetweenPatternAndStrings(DNAs,cPat)
        if cDist <= min_score :
            min_score = cDist
    Median = []
    for i in xrange(4**k):
        cPat = NumberToPattern(i,k)
        cDist = DistanceBetweenPatternAndStrings(DNAs,cPat)
        if cDist == min_score :
            Median.append(cPat)
    return Median
    
    
    
f_in = open('in.txt','r')
f_out = open('out.txt','w')
k = int(f_in.readline().strip())
DNAs = []
while True:
    Text = f_in.readline().strip()
    if (Text == None or Text == ""):
        break
    DNAs.append(Text)
print MedianString(DNAs,k)
