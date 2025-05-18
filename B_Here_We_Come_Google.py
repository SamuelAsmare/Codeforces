line1 = input()
line2 = input()
line3 = input()

# Count vowels for each line
vowels1 = line1.count("a") + line1.count("e") + line1.count("i") + line1.count("o") + line1.count("u")
vowels2 = line2.count("a") + line2.count("e") + line2.count("i") + line2.count("o") + line2.count("u")
vowels3 = line3.count("a") + line3.count("e") + line3.count("i") + line3.count("o") + line3.count("u")

# Check the vowel count conditions
if vowels1 == 5 and vowels2 == 7 and vowels3 == 5:
    print("YES")
else:
    print("NO")
