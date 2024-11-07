#!/bin/usr/env Python3




def main():
    team = input('Guess my favorite football team\n')

    testteam = team.lower()
    if testteam  == "seahawks":
         print('Thats right!')
    elif testteam == "rams":
         print('nooo wayyyy!')
        
    else:
         print('wrong!')
         break 
main()
