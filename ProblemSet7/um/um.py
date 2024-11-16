import re

def main():
    print(count(input("Text: ")))

def count(s):
 # Write regular expression testing um.. :
 # test on website  regular expression 101 - https://regex101.com/
    um_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    # print(um_list)
    # return um_list lenght in numbers
    return len(um_count)

if __name__ == "__main__":
    main()
