def get_words(text):
    return len(text.split())

def get_freq(text):
    freqs = {}
    for c in text:
        c = c.lower()
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs

def sort_on(dict):
    return dict["num"]

def sort_freqs(freqs):
    list = []
    for item in freqs:
        if item.isalpha():
            newdict = {}
            newdict["char"] = item
            newdict["num"] = freqs[item]
            list.append(newdict)
    list.sort(reverse=True, key=sort_on)
    return list

