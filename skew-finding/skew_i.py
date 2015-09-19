def skew_i(Text):
    l = list();
    C_count = 0
    G_count = 0
    for c in Text:
        l.append(G_count - C_count);
        if c == 'C':
            C_count = C_count+1
        if c == 'G':
            G_count = G_count+1
            
    l.append(G_count-C_count)
    return l

