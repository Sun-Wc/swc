from Sequence import Sequence

# create the DNASequence class
class DNASequence(Sequence):
    
    def __init__(self, id, seq):
        super().__init__(id,seq)

    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    # translate method
    def translate_seq(self):
        # codon table for translation

        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        protein = ''
        for start in range(0, len(self.seq)-2, 3):
            codon = self.seq[start:start+3]
            aa = codon_table[codon]
            protein += aa
        return protein

    def get_protein_length(self):
        # Protein length is the length of the translated sequence
        protein = self.translate_seq()
        return len(protein)

# the Protein Sequence class
class ProteinSequence(Sequence):

    def __init__(self, id, seq,description=''):
        super().__init__(id,seq)
        self._description = description

    @property
    def description(self):
        return self._description
    
    def calc_hydrophobic(self, dp=2):
        aa_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
        count = 0
        count = sum(1 for aa in self.seq if aa in aa_list)
        return round(count / len(self.seq), dp)
    
    def get_protein_length(self):
        # Protein length is simply the length of the sequence
        return len(self.seq)

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Sequence: {self.seq[:10]}..."
