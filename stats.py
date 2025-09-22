from collections import Counter

def word_count(path):
   with open (path, 'r') as file_content:
    content = file_content.read()
   return len(content.split())

def character_count(path):
     with open (path, 'r') as file_content:
        content = file_content.read()
        low = str.lower(content)
     return Counter(low)

