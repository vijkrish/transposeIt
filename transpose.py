import sys
import re

#List of chords
chord_list = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

chord_map = {
	"A": 0,
	"A#": 1,
	"B": 2,
	"C": 3,
	"C#": 4,
	"D": 5,
	"D#": 6,
	"E": 7,
	"F": 8,
	"F#": 9,
	"G": 10,
	"G#": 11
}

if (len(sys.argv) < 5):
	print "Usage: python transpose.py <input_song_file_path> <transpose_level> <output_song_file_path> <delimiter> \n"
	print "Eg: python transpose.py kaatraikonjam.txt 2 transposed_kaatraikonjam.txt \"()\""
	sys.exit()

#Read the input chord file
song_file = str(sys.argv[1])

#Read the transpose level
transpose_level = int(sys.argv[2])

#Open the song file
fp = open(song_file, "rw")

o_fp = open(str(sys.argv[3]), "w")
delimiter = str(sys.argv[4])

print delimiter

for song_line in fp:
	chord = ""
	other_line = ""
	chord_start = False

	for char in song_line:
		if char == delimiter[0]:
			chord_start = True
		elif char == delimiter[1]:
			chord_start = False
			contains_hash = False

			chord_lookup = chord[0]
			if len(chord) > 1 and chord[1] == "#":
				chord_lookup += chord[1]
				contains_hash = True

			index = chord_map[chord_lookup]
			transposedChord = chord_list[(index + transpose_level) % len(chord_list)]
			transposedChord += chord[contains_hash + 1:] 

			other_line += delimiter[0] + transposedChord + delimiter[1]
			chord = ""
		elif chord_start == True:
			chord += char
		else:
			other_line += char

	o_fp.write(other_line)
