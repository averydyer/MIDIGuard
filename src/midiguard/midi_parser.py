import mido

message = mido.Message("note_on", note=69, velocity=64)

print(message)
