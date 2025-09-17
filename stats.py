def num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")


def character_dictionary(text):
    char_dict = {}
    for character in text:
        # print(f"current character is {character.lower()}")
        if character.lower() not in char_dict:
            # print(f"in if loop: {character.lower()}")
            char_dict[character.lower()] = 1
        else:
            # print(f"in else loop: {character.lower()} count = {char_dict[character.lower()]}")
            char_dict[character.lower()] += 1
            # print(f"finish else loop: {character.lower()} count = {char_dict[character.lower()]}")
    return char_dict

def sort_on(items):
    return items["count"]

def sort_char_dict(dict):
    '''
    first take a dictionary of characters as keys and their counts as values
    create a list of dictionaries with a key char and the character as the value, and a count key and the count of the character as the value
    return a sorted list of the dictionaries using the character count values as the sorting criteria
    '''
    to_return = list()
    for item in dict:
        # print(f"{item}")
        # print(f"{item.key}")
        # print(f"{dict[item.key]}")
        if item.isalpha():
            to_return.append({"char": item, "count": dict[item]})
        # print(to_return)
    # print(to_return)
    to_return.sort(reverse=True, key=sort_on)
    # print(to_return)
    return to_return