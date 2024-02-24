import string   

def main():

    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    count_letter = count_each_letter(text)
    list_dict = dict_to_list(count_letter)
    list_dict.sort(reverse=True, key=sort_on)
    print(list_dict)
    

def get_book_text(path):

    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["count"]

def count_words(text):
    text = text.split()
    count = len(text)
    return count

def dict_to_list(dict):
    list_of_dicts = []
    for letter, count in dict.items():
        add_dict = {'letter': letter, 'count': count}
        list_of_dicts.append(add_dict)
    return list_of_dicts

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
