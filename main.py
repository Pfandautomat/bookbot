import string 

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
     
     with open("books/frankenstein.txt") as f:
         file_contents = f.read()

         word_count = len(file_contents.split())
         return word_count

def count_chars():
    with open("books/frankenstein.txt") as f:
         file_contents = f.read().lower()

    chars = {}
    alphabet_lowercase = list(string.ascii_lowercase) 

    for char in file_contents:
        if char in alphabet_lowercase:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    
    return chars

def report():
    words =  count_words()
    chars = count_chars()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words fund in the document")

    for chars,numbers in chars.items():
       print(chars,numbers)
    
    print("--- End report ---")
    




             
                 
                 

        





if __name__ == '__main__':
    #main()
    count_words()
    number_of_chars = count_chars()
    print(number_of_chars)
    report()