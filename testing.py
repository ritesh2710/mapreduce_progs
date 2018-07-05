#!/bin/python3


#if __name__ == '__main__':
#    n = int(input())

n=3

if (n%2 ==0) and (6<=n<=20):
    print("Weird")

if (n%2 == 0) and ((2<=n<6) or (n>20)):
    print("Not Weird")

if (n%2 !=0):
    print("Weird")