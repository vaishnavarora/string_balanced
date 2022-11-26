def are_balanced(s1, s2):
    return set(s1) == set(s2)

print("Enter both the strings below you want to compare they are balanced or not")
str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

print(are_balanced(str1, str2))
