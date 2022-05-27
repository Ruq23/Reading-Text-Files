# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# from importlib.resources import path


from cgitb import text


def read_file_content(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        print (contents)
        return contents
read_file_content('story.txt')


def count_words():
     text = read_file_content("./story.txt")
     counts = dict()
     words = text.split()

     for word in words:
        if word in counts:
             counts[word] += 1
        else:
             counts[word] = 1
  
     return counts 

print (count_words())



