n = int(input())
unique_chemical_compounds = set()

for _ in range(n):
    chemical_compounds = input().split()
    unique_chemical_compounds.update(chemical_compounds)

print('\n'.join(unique_chemical_compounds))