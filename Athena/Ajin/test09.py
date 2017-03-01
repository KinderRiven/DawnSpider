
str = "A/Z\\W:ZZZ<X,C>?A|XC **?"

_str = str.replace("/", "")\
    .replace("\\", "")\
    .replace(":", "")\
    .replace("<", "")\
    .replace(">", "")\
    .replace("*", "")\
    .replace("?", "")\
    .replace("\"", "")\
    .replace("|", "")

print _str