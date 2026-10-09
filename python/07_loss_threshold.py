model_name = "Swin-Tiny"
loss = 0.42
loss_limit = 0.5

print("Model:", model_name)
print("Loss:", loss)

if loss < loss_limit:
    print("Status: PASS")
else:
    print("Status: FAIL")
