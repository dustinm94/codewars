def isPalindrome(self, s: str) -> bool:
    s = [i.lower() for i in s if i.isalpha() or i.isnumeric()]
    return s == s[::-1]