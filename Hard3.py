def shortest_palindrome(s):
    rev_s = ""
    for char in s:
        rev_s = char + rev_s
    n = len(s)

    for i in range(n):
        if s[:n - i] == rev_s[i:]:
            result = rev_s[:i] + s
            return result
s = "aacecaaa"
output = shortest_palindrome(s)
print(output)
