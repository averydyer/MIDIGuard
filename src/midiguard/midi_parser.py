import mido

# creating midi object that contains data from sample midi file
midi = mido.MidiFile("samples/test_note.mid")

octave_notes = ["C", "C#", "D", "D#", "E",
                "F", "F#", "G", "G#", "A", "A#", "B"]

# message metrics variables
total_messages = 0
note_on_count = 0
note_off_count = 0
other_count = 0


def midi_number_to_note_name(number):
    # safeguard against invalid midi numbers
    if number > 127 or number < 0:
        return "ERROR: Midi number out of range."
    # remainder = position 0-11
    position = number % 12
    octave = number // 12 - 1
    note = f"{octave_notes[position]}{octave}"
    return note


# iterates through every track in file
for index, track in enumerate(midi.tracks):
    print()
    print(f"Track: {index + 1}")
    for message in track:
        total_messages += 1
        # determine message type and print relevant information
        if message.type == "note_on":
            print(f"Note started: {midi_number_to_note_name(message.note)}")
            note_on_count += 1
        elif message.type == "note_off":
            print(f"Note stopped: {midi_number_to_note_name(message.note)}")
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

# tests for midi number to note name conversion function
print(midi_number_to_note_name(60))
print(midi_number_to_note_name(64))
print(midi_number_to_note_name(69))
print(midi_number_to_note_name(72))
print(midi_number_to_note_name(48))
print(midi_number_to_note_name(150))
print(midi_number_to_note_name(-5))
print()
