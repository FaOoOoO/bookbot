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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list