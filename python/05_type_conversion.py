epoch_text = "20"
loss_text = "0.42"

epoch_text = int(epoch_text)
loss_text = float(loss_text)

next_epoch = epoch_text + 1
half_loss = loss_text / 2

print("Next epoch:", next_epoch)
print("Half loss:", half_loss)