   
def main():

    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    text = count_words(text)
    print(text)

def get_book_text(path):

    with open(path) as f:
        return f.read()

def count_words(text):
    text = text.split()
    count = len(text)
    return count

main()
