# Generate Ansible Inventory Format
# Given:
# hosts = {"web": ["web01", "web02"], "db": ["db01"]}
# Print it in an inventory-style format:
# [web]
# web01
# web02
# [db]
# db01
hosts = {"web": ["web01", "web02"], "db": ["db01"]}
for key,value in hosts.items():
    print(f"[{key}]")
    for i in value:
        print(i)
    print()
