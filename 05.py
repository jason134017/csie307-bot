words=input("input string\n")
terget=""
solution=""
for i in range(0,len(words)):
    if(words[i]!=' '):
        terget+=words[i]
    else:
        terget=terget[::-1]
        for j in range(0,len(terget)):
            if j==0:
                solution+=terget[len(terget)-1]
            elif j==len(terget)-1:
                solution+=terget[0]
            else:solution+=terget[j]
        terget=""
    #當讀到最後仍有值為處理時
    if i==len(words)-1 and terget!="":
        terget=terget[::-1]
        for j in range(0,len(terget)):
            if j==0:
                solution+=terget[len(terget)-1]
            elif j==len(terget)-1:
                solution+=terget[0]
            else:solution+=terget[j]
        terget=""
print (solution)