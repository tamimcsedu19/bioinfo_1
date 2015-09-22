
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
def hamming_distance(T1,T2):
    cnt = 0
    for c1,c2 in zip(T1,T2):
        if c1 != c2:
            cnt = cnt+1
    return cnt

def ApproxPatternCount(Pattern,Text,d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        #print Text[i:i+len(Pattern)]
        if hamming_distance(Text[i:i+len(Pattern)],Pattern) <= d:
            return True
    return False

def MotifEnumeration(DNAs,k,d):
    Patterns = set()
    for i in xrange(0,len(DNAs[0])-k+1):
        currPatterns = d_neighbourHood(DNAs[0][i:i+k],d)
        for pat in currPatterns:
            isMotif = True
            for dna in DNAs:
                if ApproxPatternCount(pat,dna,d) == False:
                    isMotif = False
                    break
            if (isMotif == True):
                Patterns.add(pat)
        
    return Patterns        


f_in = open('in.txt','r')
f_out = open('out.txt','w')
#Pat = f_in.readline().strip()
kd = f_in.readline().strip().split()
k = int(kd[0])
d = int(kd[1])
DNAs = []
while True:
    Text = f_in.readline().strip()
    if (Text == None or Text == ""):
        break
    DNAs.append(Text)

res = MotifEnumeration(DNAs,k,d)
print res
#f_out.write(str(res))

for i in res:
    f_out.write(i)
    f_out.write(' ')
          
        
    
