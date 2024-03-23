def forwardC(rules, faktaPenyakit):
    fakta = set(faktaPenyakit)

    while True:
        faktaBaru = set()
        for rule, info in rules.items():
            if all(condition in fakta for condition in info['conditions']) and info['conclusion'] not in fakta:
                faktaBaru.add(info['conclusion'])

        if not faktaBaru:
            break

        fakta.update(faktaBaru)

    return fakta


# rules penyakit
rules = {
    'R1': {'conditions': ['A', 'B'], 'conclusion': 'C'},
    'R2': {'conditions': ['C'], 'conclusion': 'D'},
    'R3': {'conditions': ['A', 'E'], 'conclusion': 'F'},
    'R4': {'conditions': ['A'], 'conclusion': 'G'},
    'R5': {'conditions': ['F', 'G'], 'conclusion': 'D'},
    'R6': {'conditions': ['G', 'E'], 'conclusion': 'H'},
    'R7': {'conditions': ['C', 'H'], 'conclusion': 'I'},
    'R8': {'conditions': ['I', 'A'], 'conclusion': 'J'},
    'R9': {'conditions': ['G'], 'conclusion': 'J'},
    'R10': {'conditions': ['J'], 'conclusion': 'K'}
}

# Fakta awal yang diketahui
faktaPenyakit = {'A', 'E'}

# Lakukan forward chaining
hasilFakta = forwardC(rules, faktaPenyakit)

# Tentukan apakah K bernilai benar
if 'K' in hasilFakta:
    print("K bernilai benar.")
else:
    print("K bernilai salah.")

print("Fakta yang dihasilkan:", ', '.join(sorted(hasilFakta)))
