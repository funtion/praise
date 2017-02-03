def caption_check(word, word_list):
    if not word.isalpha():
        return True
    return word.isupper() and word.lower() in word_list


def first_letter_caption_check(word, word_list):
    if not word.isalpha():
        return True
    return word[0].isupper and word[1:].islower() and word.lower() in word_list
