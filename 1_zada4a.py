#1
text= input()
cut_text=text[:-4]
upper_text=cut_text.upper()
alpha=upper_text.isalpha()
print(f"{upper_text}, {alpha}")

#2

text2 = input()
count = text2.count("н")
split = text2.split(" ")
upper = text2[0]
if upper == text2.upper[0]:
    print("true")
else: 
    print("false")
print(f"{count}, {split}")