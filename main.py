from stats import number_of_words, text_count, dict_sorter
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")

word_count = number_of_words(book_path)

print(f"Found {word_count} total words")

characters_found = text_count(get_book_text(book_path))
# print(characters_found)

dictionary_list = dict_sorter(characters_found)

print("--------- Character Count -------")

for dictionary in dictionary_list:
    for key in dictionary:
        if dictionary["name"].isalpha():
            print(f"{dictionary["name"]}: {dictionary["num"]}")

print("============= END ===============")
