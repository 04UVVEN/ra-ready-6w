model_name = "Swin-Tiny"
loss_text = "0.50"
loss_limit = 0.5

loss = float(loss_text)

print("Model:", model_name)
print("Loss:", loss)

if loss <= loss_limit:
    print("Status: PASS")
else:
    print("Status: FAIL")
