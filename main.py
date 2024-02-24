   
def main():

    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    count_letter = count_each_letter(text)
    print(text)

def get_book_text(path):

    with open(path) as f:
        return f.read()

def count_words(text):
    text = text.split()
    count = len(text)
    return count

def count_each_letter(text):
    alphabet = list(string.ascii_lowercase)
    letter_dict = {}
    text = text.lower()
    for letter in text:
        if letter in alphabet:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] +=1
    return letter_dict

main()
