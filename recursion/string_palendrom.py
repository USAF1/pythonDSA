def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])


print(isPalindrome("racecar"))