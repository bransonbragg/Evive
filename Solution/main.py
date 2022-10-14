from Solution.Solution import Solution 

def main():
    query = input("")
    while query:
        soln = Solution(query)
        print(soln.doOrder())
        query = input("")
      
if __name__ == '__main__':
    main()