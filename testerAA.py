def sumSequenceHelper(n):
    
    k = 0
    total = 0
    
    while k <= n:
        
        total += (pow(-1,k)) / (2*k + 1)
        k += 1 
    
    total = 4 * total
        
    return total

def sumSequence():
	
    n = 0
    N_ = 1000000
    
    while n <= N_:
        print(sumSequenceHelper(n))
        n += 1
        
def main():
	
	return sumSequence()
	
if __name__ == "__main__":
    main()