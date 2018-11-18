def numsecs(N):
    ns = 0

    other_dig = N[0:len(N) - 1]
    last_dig = N[len(N) - 1]

    while (int(other_dig) - 2 * int(last_dig) >= 0):
        ns += 1
        N = str(int(other_dig) - 2 * int(last_dig))
        # if "7" in N: ns += 1
        count7 = N.count("7")
        ns += count7

        # print(other_dig + "-" + str(2*int(last_dig)) + "=" + N)

        if len(N) == 1: break
        other_dig = N[0:len(N) - 1]
        last_dig = N[len(N) - 1]

    ns += 1

    return ns


if __name__ == "__main__":
    f = open('input2.txt')

    T = int(f.readline().strip())
    for i in range(T):
        N = f.readline().strip()

        nsec = numsecs(N)
        print("Case #" + str(i + 1) + ": " + str(nsec))
