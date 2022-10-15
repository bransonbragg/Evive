from Solution import OrderUp

def main():
    query = input("")
    soln = OrderUp(query)
    return soln.doOrder()
    
if __name__ == '__main__':
    main()