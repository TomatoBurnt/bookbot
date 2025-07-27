import sys
def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book = sys.argv[1]
        book_path = book
        text = get_book_text(book_path)
        from stats import num_word
        from stats import letter_count
        from stats import sortedlist
        dict = letter_count(text)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {book_path}...')
        print('----------- Word Count ----------')
        print(f'Found {num_word(text)} total words')
        print('--------- Character Count -------')

        for pair in sortedlist(dict):
            if pair['char'].isalpha():
                print(f'{pair['char']}: {pair['num']}')
        print('============= END ===============')
     



def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()