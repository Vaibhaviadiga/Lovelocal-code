def length_of_last_word(s):
    
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
s = "Hello World"
result = length_of_last_word(s)
print(result)
