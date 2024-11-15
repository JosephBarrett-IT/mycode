#!/bin/usr/env Python3

def main():

    vampire_count = 0   
    with open("dracula.txt", "r") as file:
        with open("vampytimex.txt","w") as newfile:
            for row in file:
                if "vampire" in row.lower():
                    print(row)
                    vampire_count += 1
                    newfile.write(row)
    print(vampire_count)














main()
