from music21 import stream, note

# Create melody
melody = stream.Stream()

notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

for n in notes:
    melody.append(note.Note(n))

# Save as MIDI
melody.write('midi', fp='generated_music.mid')

print("Music generated successfully!")