def main():
    book_path = "books/frankenstein.txt" #create .txt file that contains all the text in your book and set it to the variable book_path
    text = get_book_text(book_path)
    #print(text)
    num_words = count_words(text)
    #print(f"{num_words} words found in the document")
    num_letters = count_letters(text)
    #print(f"This is the amount of times each character is used {num_letters}")
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(" ")
    for letter, count in num_letters.items():
        print(f"The {letter} character is found {count} times") #this will be a better convention for outputting keys and values from a dictionary separately
    print("--- End report ---")
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    #print(text.split())
    return len(text.split())

def count_letters(text):
    dictionary = {}
    letters_set = set()
    for letters in text:
        if letters.isalpha():
            letters_set.add(letters.lower()) #creates an set of unique characters found in the book's text
    for set_letter in letters_set:
        letter_count = 0
        for letters in text:
            if set_letter == letters.lower(): #compares each unique letter to the lower case letters in the text
                letter_count +=1 #increases the count of each unique letter anytime it's found through the text
        dictionary[set_letter] = letter_count #sets the predefined dictionary's keys to each unique letter and its value to the letter count
    return dictionary
    
    
main()