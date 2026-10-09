model_name = "Swin-Tiny"
sample_count_text = "80"
accuracy_text = "0.91"
loss_text = "0.40"
completed = True

sample = int(sample_count_text)
accuracy = float(accuracy_text)
loss = float(loss_text)

print("Model:", model_name)
print("Sample Count:",sample)
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
elif sample < 100:
    status = "INSUFFICIENT_DATA"
elif not metrics_ok:
    status = "REVIEW"
else:
    status = "PASS"

print("Metrics OK:", metrics_ok)
print("Needs Review:", needs_review)
print("Status:", status)