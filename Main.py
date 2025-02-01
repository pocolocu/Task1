def process_string(s: str) -> tuple[str, bool]:
    vowels = "aeiouAEIOU"
    extracted_vowels = sorted(set(ch for ch in s if ch in vowels))
    contains_punctuation = any(ch in ",." for ch in s)
    return ("".join(extracted_vowels), contains_punctuation)

# Приклад використання
input_string = "abc.de,,fg"
print(process_string(input_string))  # ('ae', True)
