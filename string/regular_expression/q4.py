# Replace all digits with * in this string:
import re

txt = "Password: user123, pin: 4567"

masked=re.sub(r"\d","*",txt)
print(masked)
