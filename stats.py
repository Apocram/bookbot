def get_num_words(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def get_num_characters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        chars = {}
        for c in range(0,len(file_contents)):
            if file_contents[c] in chars:
                chars[file_contents[c]] += 1
            else:
                chars[file_contents[c]] = 1
        return chars

def sort_on(items):
    return items["num"]

def sortvert(dict):
    listed = []
    for d in dict:
        listed.append({"char": d, "num": dict[d]})
    listed.sort(reverse=True, key=sort_on)
    return listed