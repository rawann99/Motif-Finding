import itertools
from scipy.spatial.distance import hamming
l=8
t=5

def distance(dna,pro,l,n):
    len=l
    min_distance=10000000
    min_string=""
    for i in range(n-l):
        sub=dna[i:len]
        dis=hamming(sub,pro)
        if(dis<min_distance):
            min_distance=dis
            min_string=sub
        len+=1
    len=l
    return min_string
# build the profile matrix to get the min distance between all the min_strings
def total_distance(min_string,l,t,n,dna,pro):
    score = 0
    min_string=[]

    for i in range (t):
        min_string.append(distance(dna,pro,l,n))

    listtt = [0, 0, 0, 0]
    conseq = ""

    for i in range(l):
        max_list = [0, 0, 0, 0]
        coun_a = 0
        coun_c = 0
        coun_g = 0
        coun_t = 0
        # A  C   G  T
        for j in range(t):
            if (min_string[j][i] == "A"):
                coun_a += 1
                max_list[0] += 1
            if (min_string[j][i] == "C"):
                coun_c += 1
                max_list[1] += 1
            if (min_string[j][i] == "G"):
                coun_g += 1
                max_list[2] += 1
            if (min_string[j][i] == "T"):
                coun_t += 1
                max_list[3] += 1

        score += min(max_list)
    return score

def Mideian_string(l,t,n):
    dna = [[0] * 69] * 5
    for i in range (t):
        dna[i]=input("enter dna")


    pro = itertools.product(["A", "G", "C", "T"], repeat=l)
    score=100000000000
    for i in pro:
        min_dis=distance(dna,pro,l,n)
        dis=total_distance(min_dis,l,t,n,dna,pro)
        if(score>dis):
            score=dis
    print(dis)
Mideian_string(8,5,69)





