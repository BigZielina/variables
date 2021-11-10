"""
Please write a program that reads some text from the keyboard and then deletes every third character (starting with the third).
The remaining characters should be printed on the screen.

Example:

    Enter text: To be or not to be...
    Tobeorno t b..
"""

# Your code here

text = str(input("your text: "))
lst = [0]
for letter in text:
    lst.append(letter)

del lst[::3]
print("".join(lst))