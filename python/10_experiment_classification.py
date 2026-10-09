model_name = "Swin-Tiny"
accuracy_text = "0.92"
loss_text = "0.50"

accuracy = float(accuracy_text)
loss = float(loss_text)

if accuracy >= 0.90:
    accuracy_grade = "Excellent"
elif accuracy >= 0.80:
    accuracy_grade = "PASS"
else:
    accuracy_grade = "FAIL"

if loss <= 0.20:
    loss_grade = "Excellent"
elif loss <= 0.50:
    loss_grade = "PASS"
else:
    loss_grade = "FAIL"

print("Model:", model_name)
print("Accuracy:", accuracy)
print("Accuracy Grade:", accuracy_grade)
print("Loss:", loss)
print("Loss Grade:", loss_grade)