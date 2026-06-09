dna = input()
pattern = input()

cnt = 0
for i in range (len(dna)-len(pattern)+1): 
   if dna[i:i +len(pattern)] == pattern:
       cnt+=1   
print(cnt)
