   
def main():

    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):

    with open(path) as f:
        return f.read()

main()
