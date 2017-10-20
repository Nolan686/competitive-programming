# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

if __name__ == '__main__':
    N = int(raw_input())
    W = map(int, raw_input().split())
    
    W.sort(key=int)
    
    count = 0
    coins = 0
    
    x = 0
    while (x < N):
        count = 0
        for y in range(x, N):
            
            if ((W[y] - W[x]) <= 4 and (W[y] - W[x] >= 0)):
                count += 1
        if(count > 1):
            coins += 1
            x += count
        else:
            coins += 1
            x += 1
    
    print(coins)