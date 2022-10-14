from Solution.Solution import Solution 

def main():
    query = input("")
    soln = Solution(query)
    return soln.doOrder()
    
if __name__ == '__main__':
    main()