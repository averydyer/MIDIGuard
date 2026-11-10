import mido

# creating midi object that contains data from sample midi file
midi = mido.MidiFile("samples/test_note.mid")

# iterates through every track in file
# prints each track's number and all its messages
for index, track in enumerate(midi.tracks):
    print()
    print(f"Track: {index + 1}")
    for message in track:
        print(message)
print()
