initial_loss = 0.8
final_loss = 0.4
loss_drop = initial_loss - final_loss
drop_percent = (loss_drop / initial_loss) * 100

print("Loss drop:", loss_drop)
print("Drop percentage:", drop_percent)