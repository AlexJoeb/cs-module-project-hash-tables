def word_count(s):
    s = s.lower() # Lower case the entire string.
    s = ' '.join(s.split()) # Remove excessive whitespace in the middle.

    # Remove blacklisted characters.
    blacklist = ('"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&')
    list = ''.join(char for char in s if char not in blacklist).split()

    cache = {}
    for word in list:
        if word not in cache:
            cache[word] = 0
        
        cache[word] += 1

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))