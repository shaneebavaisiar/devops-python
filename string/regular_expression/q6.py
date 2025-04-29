# From this string, extract all email addresses:
import re

txt="Send reports to dev@company.com, admin@server.org"
pattern=r"[a-zA-Z0-9._@-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
l=re.findall(pattern,txt)
print(l)