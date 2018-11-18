
import sys
sys.setrecursionlimit(15000)

dicc_div = {}

def numdivisions(N):
    nd = 0

    i = 1
    while (i <= N):
        ndi = numdivisionsbynum(N,i)
        nd += ndi
        #print (str(i) + "--" + str(ndi))
        i +=1

    return nd

def numdivisionsbynum(N, num):
    if num == 1:
        return 1
    elif num == 2:
        return N//num
    else:
        nd = N//num
        while (N >= num):
            N = N - num
            i = 2
            while (i < num):
                if (N,i) in dicc_div:
                    ndi = dicc_div[(N,i)]
                else:
                    ndi = numdivisionsbynum(N, i)
                    dicc_div[(N,i)] = ndi
                #print (" > " + str(i) + "--" + str(ndi))
                i += 1
                nd += ndi
        return nd

def stack(lim, ways):
    posi = [0] * (lim + 1)
    posi[0] = 1

    for i in ways:
        #print(i)
        for k in range(i, lim + 1):
            posi[k] += posi[k - i]

    return posi[lim]



if __name__ == "__main__":
    f = open('input2.txt')
    N = int(f.readline().strip())
    np = numdivisions(N)
    print("Case #" + str(N) + ": " + str(np))
