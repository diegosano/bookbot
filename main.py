def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words_count_from_text(text)
    char_dict = get_char_count_dict(text)
    char_dict_list = chars_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")

    for char_dict in char_dict_list:
        if not char_dict["char"].isalpha():
            continue
        print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count_from_text(text):
    return len(text.split())

def get_char_count_dict(text):
    chars = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "count": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
