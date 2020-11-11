def pas(n):  
    for wers in range(1, n + 1):  
        fi = 1 
        for i in range(1, wers + 1):   
            print(fi, end = " ")  
            fi = int(fi * (wers - i) / i)  
        print("")
pas(8)