# Find all words starting with error in this log:
import re

txt = "error404 error500 warning123 error302 success"

pattern=r"error\w+"
print(re.findall(pattern,txt))
