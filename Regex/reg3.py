#sequences of lowercase letters joined by an underscore
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbb"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))
