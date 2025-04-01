def get_num_words(self): # funciton to count words in file
    count = 0 # track words
    for i in self.split(): # takes string, splits into words, counts each word.
        count += 1
    return count

def char_count(self): # function to count characters, put in dictionary
    dic_char_count = {} # init dictionary
    count = 0
    for char_count in self: # loop each chars in string
        char_lower = char_count.lower() # make all lower case
        if char_lower in dic_char_count: # check if char
            dic_char_count[char_lower] += 1 # add 1 to the value in the dictionary
        else:
            dic_char_count[char_lower] = 1 # else if new add 1
    #print(dic_char_count)

    return dic_char_count