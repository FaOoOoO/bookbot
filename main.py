from stats import word_count
from stats import character_count

def get_book_text(path):
   with open (path, 'r') as file_content:
    content = file_content.read()
    return content
   
def main():
    path = "/home/jens/Workspace/Repos/bookbot/books/frankenstein.txt"
    counted_char = character_count(path)
    #print({get_book_text(path)})
    print(f'{word_count(path)} words found in the document')
    print(f'Counted characters from Book: \n {counted_char}')

if __name__ == "__main__":
    main()


