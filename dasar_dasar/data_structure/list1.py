def count_number(numbers : list[int], target: int) -> int:
    counter = 0
    for number in numbers :
        if number == target:
            counter += number
    return counter


# find the largest word
def largest_word(words: list[str]) -> str:
    current_len = 0
    curret_word = ""
    for word in words:
        if len(word) > current_len:
            curret_word = word
            current_len = len(word)
    return f"current_len: {current_len}\ncurrent_word: {curret_word}"

print(count_number([1,1,1,1,1], 1))
print(largest_word(["hello", "world", "python", "is", "great", "program", "language"]))