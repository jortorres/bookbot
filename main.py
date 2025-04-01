from stats import get_num_words, char_count


def get_book_text(self): # function to get text from .txt file and put into string
    file_contents = ""  
    with open(self) as f:  # function to open txt file and read it, then close.
        file_contents = f.read()
    return file_contents  # return string
       
def main():  # main funciton
   # call number_of_words function with get_book_text function to get word count
   num_words = get_num_words(get_book_text("books/frankenstein.txt")) 
   num_char = char_count(get_book_text("books/frankenstein.txt"))
      
   print(f"{num_words} words found in the document")
   print(f"{num_char} characters ")

main()  # main call
