
#******************************************** METHOD 1 *********************
# file = open("sample.txt")
# contents = file.read()
# print(contents)
# file.close()


#******************************************** METHOD 2 *********************

# 1. OPEN and READ from a FILE

# with open("sample.txt") as f:
#     contents = f.read()
#     print(contents)

# 2. OPEN and WRITE to a FILE
with open("sample.txt", mode="w") as f:
    f.write("This is my new text.")
