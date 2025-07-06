#random word list

import random
alpha="abcdefghijklmnopqrstuvwxyz"
for _ in range(10):
    alpha_cp=list(alpha)
    random_word=""
    for i in range(26):
        digit=random.randint(0,len(alpha_cp)-1)
        random_alp=alpha_cp[digit]
        if random_alp not in random_word:
            random_word+=random_alp
            alpha_cp = [c  for c in alpha_cp if c != random_alp]
            break
            


     
    print(random_word)


        

