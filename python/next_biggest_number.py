#Nathan Liston 1-23-2020
#!/usr/bin/python3
import sys

def main():
    #call function to get biggest nbr
    newnum = next_biggest_number(sys.argv[1])
    print("Input: ", sys.argv[1])
    print("Output: ", newnum)


def next_biggest_number(numin):
    num = list(str(numin))
    #check to see if its possible to get a bigger number
    descending = int("".join(sorted(str(numin), reverse=True)))
    if descending <= int(numin):
        return -1
    #if it is possible to get bigger number
    else:
        for i in range(len(num) - 1, -1, -1):
            if (num[i - 1] < num[i]):
                num[i:len(num)] = sorted(num[i:len(num)])
                break
        for j in range(i, len(num)):
            if (num[i - 1] < num[j]):
                num[i - 1], num[j] = num[j], num[i - 1]
                break
        #print("returning: ", int("".join(num)))
        return(int("".join(num)))


if __name__ == "__main__":
    main()



