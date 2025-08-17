#get_words function: takes in file name, returns number of words
def get_words(f):
    file_contents = f.split()   

    return len(file_contents)

#get_characters function: takes file name, sets as a string, counts characters
def get_characters(f):
    characters = {}
    file_contents = list(str.lower(f))
    for letters in file_contents:
        if letters not in characters:
            characters[letters] = 1
        else:
            characters[letters] += 1
    return characters

