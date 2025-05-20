def get_num_words(text):
    """Counts and returns the number of words in the given text string."""
    words = text.split()
    return len(words)


def get_char_counts(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_char_counts(char_counts):
    """Takes the dictionary of character counts and returns a sorted list of dictionaries."""
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
