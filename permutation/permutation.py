from itertools import permutations 

perm = permutations(['J','E','L','E','N','É','S']) 
  
for i,word in enumerate(list(perm)): 
    print(f'{i+1}. ',"".join(word)) 