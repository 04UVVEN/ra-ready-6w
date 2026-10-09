remaining_tasks = 12
tasks_per_batch = 3
batch = 1

while remaining_tasks > 0:
    remaining_tasks = remaining_tasks - tasks_per_batch
    print("Batch:", batch, "Remaining Tasks:", remaining_tasks)
    batch = batch + 1
print("Status: FINISHED")