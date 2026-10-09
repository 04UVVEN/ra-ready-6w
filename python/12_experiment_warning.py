model_name = "Swin-Tiny"
accuracy = 0.92
loss = 0.56

print("Model:", model_name)
print("Accuracy:", accuracy)
print("Loss:", loss)

if accuracy < 0.80 or loss > 0.50:
    print("Status: REVIEW")
else:
    print("Status: OK")