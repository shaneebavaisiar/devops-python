# Merge Two Environment Variable Sets
# env1 = {"PATH": "/usr/bin", "JAVA_HOME": "/usr/lib/jvm"}
# env2 = {"JAVA_HOME": "/opt/java", "PYTHONPATH": "/usr/lib/python"}
# Merge both, giving priority to env2.

env1 = {"PATH": "/usr/bin", "JAVA_HOME": "/usr/lib/jvm"}
env2 = {"JAVA_HOME": "/opt/java", "PYTHONPATH": "/usr/lib/python"}
env1.update(env2)
print(env1)

