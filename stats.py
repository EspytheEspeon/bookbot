#get_words function: takes in file name, returns number of words
def get_words(f):
    file_contents = f.split()   

    return len(file_contents)