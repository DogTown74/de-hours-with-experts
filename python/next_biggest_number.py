#Nathan Liston 1-23-2020
#!/usr/bin/python3
import sys

def main():
    #call function to get biggest nbr
    newnum = next_biggest_number(sys.argv[1])
    print("Input: ", sys.argv[1])
    print("Output: ", newnum)


def next_biggest_number(numstr):
    n = list(str(numstr))
    print("sorted: ", sorted(n, reverse=True))
    if n == sorted(n, reverse=True):
        return -1
    else:
        for i in range(len(n) - 1, -1, -1):
            if (n[i - 1] < n[i]):
                n[i:len(n)] = sorted(n[i:len(n)])
                break
        for j in range(i, len(n)):
            if (n[i - 1] < n[j]):
                n[i - 1], n[j] = n[j], n[i - 1]
                break
        return(int("".join(n)))



if __name__ == "__main__":
    main()



