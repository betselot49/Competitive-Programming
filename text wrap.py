import textwrap

def wrap(string, max_width):
    ans = ""
    counter = 0
    for stri in string:
        ans += stri
        counter += 1
        if counter == max_width:
            ans += "\n"
            counter = 0
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
