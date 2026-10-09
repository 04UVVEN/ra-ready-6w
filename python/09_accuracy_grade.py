model_name = "Swin-Tiny"
accuracy = 0.86

print("Model:", model_name)
print("Accuracy:", accuracy)

if accuracy >= 0.90:
    print("Status: Excellent")
elif accuracy >= 0.80:
    print("Status: PASS")
else:
    print("Status: FAIL")