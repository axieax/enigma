from string import ascii_uppercase

# Enigma Rotors (alphabetic_substitution, rotation_characters)
enigma_rotors = {
    1: ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
    2: ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
    3: ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
}


# Setup board
reflector = 'ABCDEFGDIJKGMKMIEBFTCVVJAT'

# Set ciphertext
ciphertext = input('Ciphertext: ')
# Set rotors
rotors_input = [int(x) for x in input('Rotor Order (e.g. 1 2 3): ').split()]
rotors = [enigma_rotors[x][0] for x in rotors_input]
rotors_char = [ord(enigma_rotors[x][1]) - ord('A') for x in rotors_input]
# Set starting positions
starting_positions = input('Starting Positions (e.g. ABC): ')
rotors_top = [ord(pos) - ord('A') for pos in starting_positions]


# Decipher ciphertext

def solve(char_in):
    # Rotate right
    rotor_right_removed = rotors_top[2]
    rotors_top[2] = (rotors_top[2] + 1) % len(ascii_uppercase)
    if rotor_right_removed == rotors_char[2]:
        # Rotate centre
        rotor_centre_removed = rotors_top[1]
        rotors_top[1] = (rotors_top[1] + 1) % len(ascii_uppercase)
        if rotor_centre_removed == rotors_char[1]:
            # Rotate left
            rotors_top[0] = (rotors_top[0] + 1) % len(ascii_uppercase)

    # Go right to left
    relative_index = ascii_uppercase.index(char_in)
    for rotor_index in range(len(rotors) - 1, -1, -1):
        char_sub = rotors[rotor_index][(relative_index + rotors_top[rotor_index]) % len(ascii_uppercase)]
        relative_index = (ascii_uppercase.index(char_sub) - rotors_top[rotor_index] + len(ascii_uppercase)) % len(ascii_uppercase)

    # Reflector
    char_sub = reflector[relative_index]
    relative_index = [i for i, x in enumerate(reflector) if x == char_sub and i != relative_index][0]
    
    # Go left to right
    for rotor_index in range(len(rotors)):
        char_sub = ascii_uppercase[(relative_index + rotors_top[rotor_index]) % len(ascii_uppercase)]
        relative_index = (rotors[rotor_index].index(char_sub) - rotors_top[rotor_index] + len(ascii_uppercase)) % len(ascii_uppercase)

    # Output
    char_out = ascii_uppercase[relative_index]
    return char_out


# Display deciphered result
print(''.join(solve(c) for c in ciphertext))
