class Sequence:
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    @property
    def id(self):
        return self._id

    @property
    def seq(self):
        return self._seq

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return f"ID: {self.id}, Sequence: {self.seq[:10]}..."  # Preview first 10 bases

    # Common method for all sequence types
    def get_protein_length(self):
        # This method will be polymorphic, implemented differently in subclasses
        pass   
