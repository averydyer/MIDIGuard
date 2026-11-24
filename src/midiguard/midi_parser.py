import mido
# used for command line midi file selection
import sys

# creating midi object that contains data from sample midi file
midi = mido.MidiFile(sys.argv[1])

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
    # keeps track of what notes are currently on and when they started
    active_notes = {}
    # time elapsed since start of track
    absolute_time = 0
    print()
    print(f"Track: {index + 1}")
    for message in track:
        total_messages += 1
        absolute_time += message.time
        # if velocity is 0, that is considered a note_off
        if message.type == "note_on" and message.velocity > 0:
            active_notes[message.note] = absolute_time
            print(
                f"Note started: {midi_number_to_note_name(message.note)}", end=" ")
            print(f"| Time: {absolute_time} ticks")
            note_on_count += 1
        elif message.type == "note_off" or (message.type == "note_on" and message.velocity == 0):
            # only calculate duration if note was first turned on
            if message.note in active_notes:
                found_note = True
                note_duration = absolute_time - active_notes[message.note]
                del active_notes[message.note]
            else:
                found_note = False
                print(
                    f"ERROR: {midi_number_to_note_name(message.note)} Note-off signal without preceding note-on")
            print(
                f"Note stopped: {midi_number_to_note_name(message.note)}", end=" ")
            print(f"| Time: {absolute_time} ticks", end=" ")
            # do not try to print duration if note was never turned on
            if found_note:
                print(f"| Duration: {note_duration} ticks")
            else:
                print()
            note_off_count += 1
        else:
            print(f"Other event: {message.type}", end=" ")
            print(f"| Time: {absolute_time} ticks")
            other_count += 1
    # check if any notes were never ended
    if active_notes:
        for note in active_notes:
            print(
                f"WARNING: Note {midi_number_to_note_name(note)} never ended")
print()
