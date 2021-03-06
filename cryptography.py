"""
cryptography.py
Author: Ella Edmonds
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
a = input('Enter e to encrypt, d to decrypt, or q to quit: ')

while a != "q":
    if a != "q" and a != "e" and a != "d":
        print("Did not understand command, try again.")

    elif a == "e" or "d":
        b = input ("Message: ")
        c = input ("Key: ")
        
        associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    
        message= []
        for n in b:
         d = associations.find(n)
         message.append(d)
    
        key1 = []
        for n in c:
            e = associations.find(n)
            key1.append(e)
        
        #print(message)
        #print(key1)
    
        M = len(message)
        K = len(key1)
    
        key = key1*int((M/K))
        
        extra1 = M%K
        
        if extra1 != 0:
            extra = range(extra1)
            for c in extra:
                key.append(key1[c])
    
        #print(key)

        crypt1 = zip(key,message)
        crypt = []
        
        if a == "e":
            for c in crypt1:
                crypt.append(c[0]+c[1])
    
            #print(crypt)
        
            final = []
            for c in crypt:
                C = associations[c%85]
                final.append(C)
        
            #print(final)
        
            for n in final:
                print(n,end="")
            
            print()
                
        if a == "d":
            for c in crypt1:
                crypt.append(c[1]-c[0])
    
            #print(crypt)
        
            final = []
            for c in crypt:
                C = associations[c%85]
                final.append(C)
        
            #print(final)
        
            for n in final:
                print(n,end="")
                
            print()
                
    a = input('Enter e to encrypt, d to decrypt, or q to quit: ')

if a == "q":
        print("Goodbye!")


'''associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

associations.find(char)

associations[index]'''

