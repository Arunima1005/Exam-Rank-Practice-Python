def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart_score = 0  # Consonants
    kevin_score = 0   # Vowels
    length = len(string)
    
    for i in range(length):
        # Calculate how many substrings start at this index
        substrings_count = length - i
        
        if string[i] in vowels:
            kevin_score += substrings_count
        else:
            stuart_score += substrings_count
            
    # Determine and print the winner
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)