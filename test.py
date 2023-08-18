def isEven(num):
    return num%2 == 0

def isPalindrome(str):
    #mum
    left = 0
    right = len(str) - 1
    while left <= right:
        if str[left] != str[right]:
            return False
        left = left + 1
        right = right - 1
    return True

if __name__ == "__main__":
    print(isEven(2))
    print(isEven(5))
    print(isPalindrome("mum"))
    print(isPalindrome("mmmm"))
