def main():

    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """

    result = []
    value = 0

    for i in range(N + 1):
        if i == 0:
            value = 1
            result.append(value)
        else:
            value = value * 2
            result.append(value)
            
    print(result)


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
