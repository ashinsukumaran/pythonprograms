punctuation= '`.,!-@#$%^&*()_+/'
my_str=input("enter string")
no_punc=""
for char in my_str:
    if char not in punctuation:
        no_punc=no_punc+char
print(no_punc)