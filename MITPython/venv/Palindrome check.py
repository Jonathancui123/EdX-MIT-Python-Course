def IsPalindrome(s):
    def Clean(s):
        s = s.lower()
        newS = ''
        for char in s:
            if char in "abcdefghijklmnop":
                newS = newS + char
        return newS

    def Palin(s):
        print(s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and Palin(s[1:-1])
    return Palin(Clean(s))

s = input("Give palindrome: ")
print(IsPalindrome(s))


