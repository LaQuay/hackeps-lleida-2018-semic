import sys

sys.setrecursionlimit(15000)

dicc_div = {}


def numdivisions(N):
    nd = 0

    i = 1
    while (i <= N):
        ndi = numdivisionsbynum(N, i)
        nd += ndi
        # print (str(i) + "--" + str(ndi))
        i += 1

    return nd


def numdivisionsbynum(N, num):
    if num == 1:
        return 1
    elif num == 2:
        return N // num
    else:
        nd = N // num
        while (N >= num):
            N = N - num
            i = 2
            while (i < num):
                if (N, i) in dicc_div:
                    ndi = dicc_div[(N, i)]
                else:
                    ndi = numdivisionsbynum(N, i)
                    dicc_div[(N, i)] = ndi
                # print (" > " + str(i) + "--" + str(ndi))
                i += 1
                nd += ndi
        return nd


import wolframalpha


def wolfram_partitions(N):
    client = wolframalpha.Client("53L6R8-YYEQG7A92E")
    res = client.query("partitionP(" + str(N) + ")")
    return next(res.results).text


if __name__ == "__main__":
    f = open('input.txt')
    N = int(f.readline().strip())
    np = numdivisions(N)
    #np = wolfram_partitions(N)
    print("Case #" + str(N) + ": " + str(np))
