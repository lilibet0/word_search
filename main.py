def binary_search(word, wordList, low_index, high_index):
    if low_index > high_index:
        # Word is not in word list
        return False
    else:
        mid_index = (low_index 
                     + high_index) // 2

        if word == wordList[mid_index].lower():
            return True
        
        elif word < wordList[mid_index].lower():
            # Recursively search to the left of the mid point
            return binary_search(word, wordList, low_index, mid_index - 1)
        
        else:
            # Recursively search to the right of the mid point
            return binary_search(word, wordList, mid_index + 1, high_index)
        

def get_list_of_new_words(wordsTuple, wordListTuple):
    words = list(wordsTuple)
    wordList = list(wordListTuple)
    newWordList = []

    for i in words:
        if binary_search(i.lower(), wordList, 0, len(wordList) - 1) is False:
            # Word was not found in wordList
            newWordList.append(i.lower())

    return (tuple)(newWordList)


def new_words(words, wordlist):
    # Check for special cases
    if words is None or wordlist is None:
        return None
    if type(words) is not tuple or type(wordlist) is not tuple:
        return None

    return get_list_of_new_words(words, wordlist)
