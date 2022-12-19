def swap_case(s):
    ans = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                ans += char.lower()
            else:
                ans += char.upper()
        else:
            ans += char         
    return ans
