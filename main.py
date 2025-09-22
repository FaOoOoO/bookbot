
def get_book_text(path):
   with open (path, 'r') as file_content:
    content = file_content.read()
    return content
   
def word_count(path):
   with open (path, 'r') as file_content:
    content = file_content.read()
   return len(content.split())

def main():
    path = "/home/jens/Workspace/Repos/bookbot/books/frankenstein.txt"
    #print({get_book_text(path)})
    print(f'{word_count(path)} words found in the document')
    
if __name__ == "__main__":
    main()


