#!/usr/bin/env python3
import random

def main():

    wordbank= ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    tlgstudents.append(4)

    num = int(input("Pick a number 0-20\n"))

    student_name = tlgstudents[num]

    name = random.choice(tlgstudents)

    print(f"\n {name} always uses {tlgstudents[-1]} {wordbank[1]} to indent")




main()
