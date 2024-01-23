text=input("Enter some text: ")
index = text.find("the") != 1
if index !=-1:
    # print("This sentence contains the word 'the'")
    print("It is located at index", index)
else:
    print("This sentence does not contain the word 'the'")