def main():

    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """

    result = 0
    
    for i in range(N + 1):
        if i == 0:
            result = 1
            print(result, end= " ")
        else:
            result = result * 2
            print(result, end= " ")


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
