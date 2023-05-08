sentence = "My name is William"

# Format string
print(f"This is the sentence: \"{sentence}\"")

# Check length
print("Length: " + str(len(sentence)))

# Check if something is in a sentence
print("\"name\" is in sentence: " + str("name" in sentence))

# Find the place of a substring
print("\"is\" is at: " + str(sentence.find("is")))

# To upper case
print("Upper case: " + sentence.upper())
print("Title: " + sentence.title())

print()
print(sentence[3:7])
print(sentence[11:])
print(sentence[11:-1])