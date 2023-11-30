def isPalindrome(s: str) -> bool:
    # print(s)
    lowered = upper_to_lower(s)
    # print(lowered)
    removed = remove_non_alpha(lowered)
    # print(removed)
    reverse = reversed(removed)
    # print(reverse)
    return reverse == removed

def upper_to_lower(s: str):
    return s.lower()

def remove_non_alpha(s: str):
    new_list = []
    for e in s:
        if e.isalnum():
            new_list.append(e)
    new_string = ''.join(new_list)
    return str(new_string)

def reversed(s: str):
    return s[::-1]


# input_string = "A man, a plan, a canal: Panama"
# input_string = "race a car"
input_string = ""
print(isPalindrome(input_string))
# print(upper_to_lower(input_string))
# print(remove_non_alpha(input_string))
# print(reversed(input_string))
