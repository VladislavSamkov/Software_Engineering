value = input("Write something: ")
print(len(value))

lowercase_sentence = value.lower()
print(lowercase_sentence)

vowels = 'aeiou'
print(sum(1 for char in lowercase_sentence if char in vowels))

replaced_sentence = lowercase_sentence.replace("ugly", "beauty")
print(replaced_sentence)

starts_with_the = value.startswith("The")
ends_with_end = value.endswith("end")
print(f"Начинается с 'The': {starts_with_the}")
print(f"Заканчивается на 'end': {ends_with_end}")