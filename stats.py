def get_num_words(num): # funciton to count words in file
    count = 0 # track words
    for i in num.split(): # takes string, splits into words, counts each word.
        count += 1
    return count

def char_count(char): # function to count characters, put in dictionary
    dic_char_count = {} # init dictionary
    
    for char_count in char: # loop each chars in string
        char_lower = char_count.lower() # make all lower case
        if char_lower in dic_char_count: # check if char
            dic_char_count[char_lower] += 1 # add 1 to the value in the dictionary
        else:
            dic_char_count[char_lower] = 1 # else if new add 1
    return dic_char_count

def sort_on(dict): # return key
    return dict["count"]

def sort_list(dict): # sort dictionary by key
    resultList = []
    for key, val in dict.items():
        char_dict = {"character": key, "count": val} # put in new list
        resultList.append(char_dict) # add to list
    resultList.sort(reverse=True, key=sort_on) # sort
      
    return resultList