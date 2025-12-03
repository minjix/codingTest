def palindrome(data):
    if len(data) == 1:
        print("o")
        return True
    
    if data[0] == data[-1]:
        palindrome(data[1:-1])
    else:
        print("x")
        return False


palindrome('level')
palindrome('data')