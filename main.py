def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    counts = count_words(text)
    letters_dict = count_letters(text)
    list_letters = list(letters_dict.items())
    list_letters.sort(key=lambda x: x[1], reverse=True)

    print(f'\n--- Begin report of {book_path} ---')
    print(f"{counts} words found in the document \n")
    for item in list_letters:
        if item[0].isalpha():
            print(f'The \'{item[0]}\' character was found {item[1]} times')
    print(f'\n--- End report --- \n')

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def count_words(text):
    counts = 0
    words = text.split()
    
    for i in range(0, len(words)):
        counts += 1;
    return counts

def count_letters(text):
    letters = {}
    text = text.lower()

    for item in text:

        if item in letters:
            letters[item] += 1
        else:
            letters[item] = 1
    
    return letters


main()
