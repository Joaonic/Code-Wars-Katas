import string
def DNA_strand(dna):
    norm = str.maketrans('CTAG', 'GATC')
    return dna.translate(norm)