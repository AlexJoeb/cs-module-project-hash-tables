import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

    # TODO: analyze which words can follow other words
    cache = {}
    indx = 0
    for word in words:
        if indx == len(words) - 1: break
        
        if word not in cache:
            cache[word] = []
        
        cache[word].append(words[indx + 1])
        indx += 1

    # TODO: construct 5 random sentences
    sentences = []

    def form_sentence(sentence, current_word=None):
        def format_sentence(s): return s.strip()[0].upper() + s.strip()[1:]
        
        if current_word == None:
            current_word = words[random.randint(0, len(words) - 1)]

        # Append current word to sentence.        
        sentence += f' {current_word}'

        # Determine next word.
        possibles = cache[current_word]

        if len(possibles) <= 0:
            return format_sentence(sentence)
        else:
            next_word = possibles[random.randint(0, len(possibles) - 1)]
            if next_word[-1] == '.':
                sentence += f' {next_word}'
                return format_sentence(sentence)
            return form_sentence(sentence, next_word)
    
    final = form_sentence("")
    print(final)

