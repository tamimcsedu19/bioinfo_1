import skew_i;
def min_skew(Text):
    l = skew_i.skew_i(Text);
    min_val = max(l)
    min_skews = []
    for i in xrange(len(l)):
        if l[i] == min_val:
            min_skews.append(i)
    return min_skews;

print min_skew('CATTCCAGTACTTCATGATGGCGTGAAGA')
'''
f_in = open('in.txt','r')
f_out = open('out.txt','w')
Text = f_in.readline().strip()
res = min_skew(Text)
for i in res:
    f_out.write(str(i))
    f_out.write(' ')
'''
