import mido

# creating midi object that contains data from sample midi file
midi = mido.MidiFile("samples/test_note.mid")

# message metrics variables
total_messages = 0
note_on_count = 0
note_off_count = 0
other_count = 0

# iterates through every track in file
for index, track in enumerate(midi.tracks):
    print()
    print(f"Track: {index + 1}")
    for message in track:
        total_messages += 1
        # determine message type and print relevant information
        if message.type == "note_on":
            print(f"Note started: {message.note}")
            note_on_count += 1
        elif message.type == "note_off":
            print(f"Note stopped: {message.note}")
            note_off_count += 1
        else:
            print(f"Other event: {message.type}")
            other_count += 1
print()

print("MIDI Analysis Summary")
print("---------------------")
print(f"Total messages: {total_messages}")
print(f"Note-on messages: {note_on_count}")
print(f"Note-off messages: {note_off_count}")
print(f"Other messages: {other_count}")
print()
