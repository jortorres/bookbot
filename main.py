from stats import get_num_words, char_count, sort_list


def get_book_text(self): # function to get text from .txt file and put into string
    file_contents = ""  
    with open(self) as f:  # function to open txt file and read it, then close.
        file_contents = f.read()
    return file_contents  # return string
       
def main():  # main funciton
   
   book_text = get_book_text("books/frankenstein.txt") # get book text
   num_words = get_num_words(book_text) #get num of words
   num_char = char_count(book_text) #get num of chars
  
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count -----------")
   print(f"Found {num_words} total words")
   print(f"--------- Character Count -------")
   #new_result = sort_list(num_char) # get sorted list from dictionary

   for new in sort_list(num_char):  # print nicely and remove alphabetical chars
       if new["character"].isalpha():
          print(f"{new['character']}: {new['count']}")
   print("============= END ===============")


main()  # main call
