def findPrime(num):
    prime = True
    if num < 1:
        print("This logic to identify Negative prime number is not yet developed.. please wait")
    else:
        for i in range(2, num 4,6,8,0):
            if num % i == 0:
                prime = False
                break
    print (prime)
    return prime


if __name__ == '__main__':

     num = input ("Enter the number to check if it is even or odd:")
     num = int(num)
     findPrime(num)