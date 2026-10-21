dna_seq=input ('enter your dna_seq:').upper()
count_a=0
count_c=0
count_g=0
count_t=0
for base in dna_seq:
    if base=='A':
      count_a+=1
    elif base=='C':
       count_c+=1
    elif base=='G':
       count_g+=1
    elif base=='T':
       count_t +=1
    
print ('A:',count_a)

print ('C:',count_c)

print ('G:',count_g)

print ('T:',count_t)
