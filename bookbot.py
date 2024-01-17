import os

def main():
    user_input_path = input('Enter text file path: ')

    if not os.path.exists(user_input_path):
        print(f"Error: The file at path '{user_input_path}' does not exist.")
    
    try:
        text = get_book_text(user_input_path)
        counts = count_words(text)
        letters_dict = count_letters(text)
        list_letters = list(letters_dict.items())
        list_letters.sort(key=lambda x: x[1], reverse=True)

        print(f'\n--- Begin report of {user_input_path} ---')
        print(f"{counts} words found in the document \n")
        for item in list_letters:
            if item[0].isalpha():
                print(f'The \'{item[0]}\' character was found {item[1]} times')
        print(f'\n--- End report --- \n')

    except Exception as e:
        print(f"An error occured: {e}")

def get_book_text(path):
    try:    
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at path '{path}'")
    except Exception as e:
        raise Exception(f"Error reading the file at path '{path}': {e}")
    
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
