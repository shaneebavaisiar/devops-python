# Retry SSH connection until success
# (Simulate with a list of results: ["fail", "fail", "success"])
# ✅ Goal:
# Keep printing "Trying SSH..." until the result is "success".
# Then print "Connected!" and stop.

results=["fail", "fail", "success"]
index=0
while index<len(results) and results[index]!="success":
    print(f"Trying SSH...")
    index+=1
if index<len(results):
    print(f"connected")


# or

# for i in results:
#     if i!="success":
#         print(f"Trying SSH...")
#     else:
#         print(f"connected")
#         break