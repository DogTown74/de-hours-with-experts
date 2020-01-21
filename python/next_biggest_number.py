#Nathan Liston 1-23-2020
#!/usr/bin/python3
import sys

def main():
    #get the nbr passed
    num = sys.argv[1]
    print("Input: ", num)
    #call function to get biggest nbr
    newnum = next_biggest_number(num)
    if newnum > int(num):
        print("Output: ", newnum)
    else:
        print("Output: ", -1)


def next_biggest_number(num):
    #reorder the nbr
    descending = int("".join(sorted(str(num), reverse=True)))
    return descending

if __name__ == "__main__":
    main()



