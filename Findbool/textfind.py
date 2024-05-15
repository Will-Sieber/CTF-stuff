text = "Give me a word that isn't in this sentence"
print(text)
word = input().split(" ")[0]
if word == "":
    print("That's not a word")
    exit()
if text.find(word):
    print(f"this word is in this sentence according to text.find(word)")
else:
    print("Wooo nice")