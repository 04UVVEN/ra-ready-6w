remaining_tasks = 11
batch_capacity = 4
batch = 0
total_processed = 0

while remaining_tasks > 0:
    batch = batch + 1
    if remaining_tasks >= batch_capacity:
        processed = batch_capacity
    else:
        processed = remaining_tasks
    remaining_tasks = remaining_tasks - processed
    print("Batch:", batch, "Processed:", processed, "Remaining:", remaining_tasks)
    total_processed = total_processed + processed
print("Total Batches:", batch)
print("Total Processed:", total_processed)
print("Status: FINISHED")