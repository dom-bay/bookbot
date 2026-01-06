def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    text = text.lower()
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]


def get_sorted_character_counts(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            chars_list.append({
                "char": char,
                "num": count
            })

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


    