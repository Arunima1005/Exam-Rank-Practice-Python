## using sort and sorted

# def count_vowel(word):
#     count = 0
#     for c in word:
#         if c.lower() in "aeiou":
#             count += 1
#     return count


# def cryptic_sorter(strings):
#     return sorted(
#         strings,
#         key=lambda s: (
#             len(s),
#             s.lower(),
#             count_vowel(s),
#             s
#         )
#     )

def count_vowel(word: str) -> int:
    count = 0
    for c in word:
        if c.lower() in "aeiou":
            count += 1
    return count


def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)

    for i in range(n):
        for j in range(i + 1, n):

            # Rule 1: shorter string first
            if len(strings[i]) > len(strings[j]):
                strings[i], strings[j] = strings[j], strings[i]

            # Rule 2: alphabetical (case-insensitive)
            elif len(strings[i]) == len(strings[j]):
                if strings[i].lower() > strings[j].lower():
                    strings[i], strings[j] = strings[j], strings[i]

                # Rule 3: vowel count
                elif strings[i].lower() == strings[j].lower():
                    if count_vowel(strings[i]) > count_vowel(strings[j]):
                        strings[i], strings[j] = strings[j], strings[i]
                    if strings[i] > strings[j]:
                        strings[i], strings[j] = strings[j], strings[i]

    return strings


print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))

#### AI Solution based on mine
# def count_vowel(word: str) -> int:
#     count = 0
#     for c in word:
#         if c.lower() in "aeiou":
#             count += 1
#     return count


# def cryptic_sorter(strings: list[str]) -> list[str]:
#     n = len(strings)

#     for i in range(n):
#         for j in range(i + 1, n):

#             if len(strings[i]) > len(strings[j]):
#                 strings[i], strings[j] = strings[j], strings[i]

#             elif len(strings[i]) == len(strings[j]):

#                 if strings[i].lower() > strings[j].lower():
#                     strings[i], strings[j] = strings[j], strings[i]

#                 elif strings[i].lower() == strings[j].lower():

#                     if count_vowel(strings[i]) > count_vowel(strings[j]):
#                         strings[i], strings[j] = strings[j], strings[i]

#     return strings




#print(count_vowel("Apaple"))
# 
# ### INcorrect
# def count_vowel(strs):
#     count = 0
#     for s in strs:
#           if s.lower() in "aeiou":
#                count += 1
#     return count
# def cryptic_sorter(strings: list[str]) -> list[str]:
#     for i in range(len(strings)):
#         for j in range(i+1,len(strings)):
#             if len(strings[i]) > len(strings[j]):                
#                 strings[i], strings[j] = strings[j], strings[i]
#             elif len(strings[i]) == len(strings[j]):
#                 if strings[i].lower() > strings[j].lower():
#                         strings[i], strings[j] = strings[j], strings[i]
#                 elif strings[i].lower() == strings[j].lower():
#                      if count_vowel(strings[i]) > count_vowel(strings[j]):
#                         strings[i], strings[j] = strings[j], strings[i]

#     return strings



