from stats import get_book_text,get_word_count, char_dict, sort_into_list_of_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
text = get_book_text(book_path)

word_count = get_word_count(text)
char_dict = char_dict(text)


list_of_dict = sort_into_list_of_dict(char_dict)

print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
''')
for entry in list_of_dict:
    if entry["char"].isalpha():
        print(f"{entry['char']}: {entry['num']}")
print(f'''
============= END ===============
''')