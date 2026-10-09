model_name = "Swin-Tiny"
accuracy = 0.88
loss = 0.45
completed = True

print("Model:", model_name)
print("Accuracy:", accuracy)
print("Loss:", loss)
print("Completed:", completed)

if accuracy >= 0.85 and loss <= 0.50:
    metrics_ok = True
else:
    metrics_ok = False

if accuracy < 0.85 or loss > 0.50:
    needs_review = True
else:
    needs_review = False

if not completed:
    status = "RUNNING"
elif metrics_ok:
    status = "PASS"
else:
    status = "REVIEW"

print("Metrics OK:", metrics_ok)
print("Needs Review:", needs_review)
print("Status:", status)