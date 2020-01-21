#!/usr/bin/python3
import sys

def main():
    parm = sys.argv[1]
    nbr = int(sys.argv[1])
    nbrlen = len(sys.argv[1])
    biggestnbr = 0
    descending = "".join(sorted(str(parm), reverse=True))
    print("desc", descending)
    #for loop to loop through the nbr
    for x in reversed(range(nbrlen)):
            print("nbrlen",x)
            print(parm[:(x+1)])
            print("next biggest nbr", next_biggest_number(parm[:(x+1)]))
    else:
            print("finished Loop 1")
    #  print(next_biggest_number())
    print("im in main")
    print(sys.argv[1])
    #next_biggest_number(1)
    return 0


def next_biggest_number(num):
    print("im in next biggest number", num)
    bignbr = 0
    for c in str(num):
        i = int(c)
        if i > bignbr:
            bignbr = i
            print("bignbr is now", bignbr)
    #else:
    #    print("finished loop2")
    print("returning", bignbr)
    return bignbr

if __name__ == "__main__":
    main()




