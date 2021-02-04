def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = sentence_counter(text)
    total_syllables = syllables_counter(words)
    score = (206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words))

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
    print('readability score is', score)
    output_result(score)


def sentence_counter(text):
    count = 0
    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count = count + 1

    return count


def output_result(score):
    if score >= 90.0:
        print('Reading level of 5th Grade')
    elif score >= 80.0:
        print('Reading level of 6th Grader')
    elif score >= 70.0:
        print('Reading level of 7th Grader')
    elif score >= 60.0:
        print('Reading level of 8-9th Grader')
    elif score >= 50.0:
        print('Reading level of 10-12th Grader')
    elif score >= 30.0:
        print('Reading level of College Student')
    else:
        print('Reading level of College Grad')


def syllables_counter(words):
    count = 0
    for word in words:
        syllables_count = syllables_checker(word)
        count = count + syllables_count

    return count


def syllables_checker(word):
    count = 0

    endings = '.,!?;:'

    last_char = word[-1]
    if last_char in endings:
        new_word = word[:-1]
    else:
        new_word = word

    if len(new_word) <= 3:
        return 1

    if new_word[-1] in 'eE':
        new_word = new_word[:-1]

    vowels = "aeiouAEIOU"
    prev_char_vowel = False
    for char in new_word:
        if char in vowels:
            if not prev_char_vowel:
                count = count + 1
            prev_char_vowel = True
        else:
            prev_char_vowel = False

    if new_word[-1] in 'yY':
        count = count + 1

    return count


if __name__ == "__main__":
    import ch1text

    print('Chapter1 Text: ')
    compute_readability(ch1text.text)
