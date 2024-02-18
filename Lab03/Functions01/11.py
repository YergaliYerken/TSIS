def palindrome(s):
    ss=s[::-1]
    if s == ss:
        print("it's palindrome")
    else:
        print("No palindrome")

palindrome(str(input()))


