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
            print(f"The value of 2 to the power of 0 is {result}")
        else:
            result = result * 2
            print(f"The value of 2 to the power of {i} is {result}")


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
