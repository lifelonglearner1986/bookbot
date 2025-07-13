def number_of_words(filepath):
    with open(filepath) as f:
        file_contents = f.read().split()
    return len(file_contents)

def text_count(book_text):
    char_counts = {}
    for char in book_text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def dict_sorter(dictionary):

    sorted_list = []

    for name in dictionary:
        count = dictionary[name]
        sorted_list.append({"name": name, "num": count})
        
    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list
        