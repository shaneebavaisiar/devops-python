# Keep removing completed jobs from a queue
jobs = ["build", "test", "deploy"]
while jobs:
    print(f"completed the job: {jobs.pop(0)}")
else:
    print(f"all jobs completed")