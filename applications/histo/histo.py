import pprint

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)

with open("robin.txt") as file:
    def sanatize(s):
        s = " ".join(s.strip().lower().split()) # Remove all excessive whitespace and lower-case.
        ignore = ('"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&')
        s = "".join([ltr for ltr in s if ltr not in ignore]) # Remove all `ignore` characters.
        return s

    words = sanatize(file.read()).split() # Sanatize and split words into an array.

    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    sorted_by_count = sorted([(v, k) for i, (k, v) in enumerate(counts.items())], key=lambda x: x[0], reverse=True)
    
    values = {}

    for pair in sorted_by_count:
        if pair[0] not in values:
            values[pair[0]] = []
        
        values[pair[0]].append(pair[1])
    
    for idx, (key, list) in enumerate(values.items()):
        values[key] = sorted(list)

    values = sorted(values.items(), reverse=True)

    for tup in values:
        for word in tup[1]:
            hashes = ['#'] * tup[0]
            print(f'{word} | {"".join(hashes)}')