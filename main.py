def get_book_text(self): # function to get text from .txt file and put into string
    file_contents = ""  
    with open(self) as f:  # function to open txt file and read it, then close.
        file_contents = f.read()
    return file_contents  # return string

def number_of_words(self): # funciton to count words in file
    count = 0 # track words
    for i in self.split(): # takes string, splits into words, counts each word.
        count += 1
    return count
        

def main():  # main funciton
   #words = get_book_text("books/frankenstein.txt")
   num_words = number_of_words(get_book_text("books/frankenstein.txt"))
   print(f"{num_words} words found in the document")

main()  # main call

    