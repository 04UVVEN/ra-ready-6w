epochs = 4
first_epoch_images = 20
increase_per_epoch = 10
min_images = 40
qualified_epochs = 0

images = first_epoch_images
total = 0

for i in range(1, epochs + 1):
    total = total + images
    if images >= min_images:
        status = "PASS"
        qualified_epochs = qualified_epochs + 1
    else:
        status = "LOW"
    print("Epoch:", i, "Images:", images, "Total:", total, "Status:", status)
    images = images + increase_per_epoch

print("Qualified Epochs:", qualified_epochs)
print("Total Images:", total)