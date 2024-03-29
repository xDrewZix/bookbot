import string   

def main():

    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    count_letter = count_each_letter(text)
    list_dict = dict_to_list(count_letter)
    list_dict.sort(reverse=True, key=sort_on)
    sorted_dict = list_to_dict(list_dict)

    for letter, count in sorted_dict.items():
        print(f"The '{letter}' character was found {count} times")
    

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
    '''changes the dict into a list of dictionaries for easier sorting'''
    list_of_dicts = []
    for letter, count in dict.items():
        add_dict = {'letter': letter, 'count': count}
        list_of_dicts.append(add_dict)
    return list_of_dicts

def list_to_dict(listdict):
    '''changes the list back to a dictionary for easier iteration in main() for-loop.'''
    sorted_dict = {}
    for i in listdict:
        sorted_dict[i['letter']] = i['count']
    return sorted_dict


def count_each_letter(text):
    '''adds each letter as a key and its count as value to a dictionary
    alphabet is compared against the letter to make sure it is a letter.'''
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
