model_name = "Swin-Tiny"
image_count_text = "180"
duration_text = "7.5"

image_count = int(image_count_text)
duration = float(duration_text)
throughput = image_count / duration
output = "Throughput: " + str(throughput) + " images/s"

print("Model:", model_name)
print("Images:", image_count)
print("Duration:", duration)
print(output)