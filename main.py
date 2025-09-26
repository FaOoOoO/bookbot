from stats import word_count, character_count, chars_dict_to_sorted_list
import sys




def get_book_text(path):
   with open (path, 'r') as file_content:
    content = file_content.read()
    return content
   
def print_report(path, counted_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



def main():
    path= sys.argv[1]
    if len(sys.argv) != 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else: 
        counted_char = character_count(path)
        counted_words = word_count(path)
        chars_sorted_list = chars_dict_to_sorted_list(counted_char)
        print_report(path, counted_words, chars_sorted_list)


if __name__ == "__main__":
    main()


