def roman_to_hindu_arabic_numeral(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    hindu_arabic_numeral = 0

    # Go through all characters in roman number except the last
    for i in range(0, len(s)-1):
        current_roman_digit = roman_dict[s[i]]
        next_roman_digit = roman_dict[s[i+1]]

        # Add or subtract based on the hindu arabic numeral value of next character compared to current character
        if current_roman_digit < next_roman_digit:
            hindu_arabic_numeral -= current_roman_digit
        else:
            hindu_arabic_numeral += current_roman_digit

    # Add hindu arabic numeral value of last character
    last_roman_digit = roman_dict[s[-1]]
    hindu_arabic_numeral += last_roman_digit

    return hindu_arabic_numeral


print(roman_to_hindu_arabic_numeral("MCMXCIV"))
