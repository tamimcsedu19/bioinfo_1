from __future__ import division
alphabets = ['A','C','G','T']

def SymbolToNumber(S):
    D = {'A':0,'C':1,'G':2,'T':3}
    return D[S]
def NumberToSymbol(N):
    NtoS = {0:'A',1:'C',2:'G',3:'T'}
    return NtoS[N]
def Profile_most_Probable_Kmer(Profile,Text,k):
    '''
        Proifle is a Dictionary with keys 'ATCG'
        
    '''
    prMax = float('0')
    most_probable_kmer = ''
    for i in xrange(len(Text)-k+1):
        cText = Text[i:i+k]
        
        pr = 1
        for j in xrange(k):
            pr = pr*Profile[cText[j]][j]
        if i == 0 or pr > prMax:
            prMax = pr
            most_probable_kmer = cText
    return most_probable_kmer
    
def updateProfile(ProfileC,Text,prev,printNow):
    Profile = ProfileC
    for i in xrange(len(Text)):
        for c in alphabets:
            Profile[c][i] = Profile[c][i]*prev+1
        Profile[Text[i]][i] = Profile[Text[i]][i]+1
        for c in alphabets:
            Profile[c][i] = Profile[c][i]/(prev+1)
       
    return Profile
    
        
def score(Motifs):
    total_score = 0
    
    for j in xrange(len(Motifs[0])):
        cnt = [0]*4
        for i in xrange(len(Motifs)):
            cnt[SymbolToNumber(Motifs[i][j])] =  cnt[SymbolToNumber(Motifs[i][j])]+1
        total_score = total_score + len(Motifs)-max(cnt)
    
    return total_score
           
        
def GREEDYMOTIFSEARCH(DNAs,k,t):
    Profile = {}
    for c in alphabets:
        Profile[c] = [1]*k
    BestMotifs = []
    for S in DNAs:
        BestMotifs.append(S[0:k])
    bestScore = score(BestMotifs)
    for i in xrange(len(DNAs[0])-k+1):
        Profile = {}
        for c in alphabets:
            Profile[c] = [1]*k
        cMotifs = []
        cMotifs.append(DNAs[0][i:i+k])
        for j in xrange(1,len(DNAs)):
            if i == 6 and j == 3:
                Profile = updateProfile(Profile,cMotifs[j-1],j,True)
            else:
                Profile = updateProfile(Profile,cMotifs[j-1],j,False)
            mostProb = Profile_most_Probable_Kmer(Profile,DNAs[j],k)
            cMotifs.append(mostProb)
      
        cScore = score(cMotifs)
        if cScore < bestScore:
            BestMotifs = cMotifs
            bestScore = cScore
    
    return BestMotifs
            
        
        
        
        




f_in = open('in.txt','r')
f_out = open('out.txt','w')
kd = f_in.readline().strip().split()
k = int(kd[0])
d = int(kd[1])
DNAs = []
while True:
    Text = f_in.readline().strip()
    if (Text == None or Text == ""):
        break
    DNAs.append(Text)
l= GREEDYMOTIFSEARCH(DNAs,k,d)
for i in l:
    print i,
