def get_num_words(self): # funciton to count words in file
    count = 0 # track words
    for i in self.split(): # takes string, splits into words, counts each word.
        count += 1
    return count

def char_count(self):
    dic_char_count = {}

    for char_count in self:
        char_lower = char_count.lower()
        dic_char_count[char_lower] = 1

    print(dic_char_count)

    return None 