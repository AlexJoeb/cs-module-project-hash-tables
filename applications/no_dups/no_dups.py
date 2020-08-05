def no_dups(s):
    list = s.split(' ')
    cache = []
    for word in list:
        if word not in cache:
            cache.append(word)
    
    return " ".join(cache)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))