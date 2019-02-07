

# In[34]:


def apriori(data='trans_clean.txt', support= 5, name = 'cs634_KaranSingh_apriori_n'):
    
    with open(data) as f:
        data = [line.rstrip() for line in f]
    
    piles= []  
    
    Ck = C1(data, support)

    piles.append(Ck)
    PriorCk = Ck.keys()
    L1 = Ck.keys()
    
    piles = AprioriCalculation(piles,PriorCk, L1,data, support,Ck)
    
    write(piles,name)
    
    return piles
      


# In[35]:


def AprioriCalculation(piles,PriorCk, L1,data, support,Ck):
    condition = True
    k = 2
    
    while condition != False:
        newCK = CK(PriorCk, L1, k)
        values = {}

        
        for d in data:
            
            z = d.split(" ")
            z = set(z)
            
            for c in newCK:
                potentialcand = set(c)
                cross = potentialcand.intersection(z)
                
                if len(cross) == k:
                    try:
                        values[str(c)] += 1
                    except:
                        values[str(c)] = 1
                        
        k = k + 1
        
        if values == {}:
            condition = False
            statement1 = "Can not combine any more values at "
            print(statement1 + str(k))
        
        else:
            
            Output2 = {k: v for k, v in values.items() if v >= support}

            PriorCk = list(Output2.keys())
            
            for i, c in enumerate(PriorCk):
                
                PriorCk[i] = eval(c)
                
                piles.append(Output2)


    return piles


    


# In[36]:


# Performs a first pass on the data, returns a dictionary
# with counts
def C1(data, support):

    C = {}
    
    for d in data:
        val = d.split(" ")
        val = set(val)
        for v in val:
            try:
                C[v] += 1
            except:
                C[v] = 1
    
        CMod = Filter(C,support)
    return CMod


# In[37]:


def Filter(C, support):
    CMod = {key: value for key, value in C.items() if value >= support}  
    
    return CMod
    


# In[38]:


def CK(PriorCk, L1, k):

    combine = [(x ,y) for x in PriorCk for y in L1]
    
    NewCK = []
    
    forget = []
    
    for can in combine:
        new = []
        
        for i in can:
            if isinstance(i, tuple):
                for item in i:
                    new.append(item)
            else:
                new.append(i)
        NewCK.append(tuple(new))
        
        for i, can in enumerate(NewCK):
            
            NewCK[i] = set(can)
            NewCK[i] = tuple(NewCK[i])

            if len(NewCK[i]) < k:
                forget.append(i)
    
    New_CK_Again = CKRepeat(NewCK, forget)
            
    return New_CK_Again


# In[39]:


def CKRepeat(NewCK, forget):
    New_CK_Again = [x for y, x in enumerate(NewCK) if y not in forget]
    New_CK_Again = list(set(New_CK_Again))
    return New_CK_Again
    


# In[40]:


def write(layers,name):
    output = layers
    with open(name +".txt", 'w') as f:
        f.write('o')
        for b in output:
            for k,v in b.items():
                f.write('%s:%s\n' % (k, v))
    f.close()


# In[42]:


import sys


first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]


apriori(data= str(first_arg), support= int(second_arg), name= str(third_arg))

