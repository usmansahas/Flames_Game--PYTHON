                                                       #FLAMES GAME
name1=input("Enter First Name: ")
name2=input("Enter Second Name: ")
if name1.isalpha() and name2.isalpha():
    print("Names Accepted :)")
else:
    print("Enter Valid Names without spaces and any other Characters :(")

l1=list(name1)
l2=list(name2)
non_common_str=[]
for i in l1:
    if i in l2:
        l2.remove(i)
    else:
        non_common_str.append(i)

non_common_str.extend(l2)
print(f"Non Common letters from both names are '{"".join(non_common_str)}'")
print(f"Total Non Common Letters from Both names = {len(non_common_str)}")


word=list("FLAMES")
meaning={"F":"Friends",
         "L":"Love",
         "A":"Affection",
         "M":"Marriage",
         "E":"Enemies",
         "S":"Sisters"}
count=len(non_common_str)
idx=0
while len(word) > 1:
    idx = (idx + count - 1) % len(word)
    word.pop(idx)
for i in meaning.keys():
    if i==word[0]:
        print(f"you got a Match as {i} which means '{meaning[i].upper()}'")

