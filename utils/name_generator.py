import string

class NameGenerator:
    """
    A class to generate unique sequential names consisting of letters. 
    Names start as "A", "B", ..., "Z" and continue as "AA", "BB", etc., once the alphabet is exhausted.
    """

    def __init__(self):
        """
        Initializes the NameGenerator instance with a counter and an alphabet list.
        
        Attributes:
            counter (int): Tracks the number of names generated, used to determine the next name.
            alphabet (list): A list of uppercase letters from 'A' to 'Z'.
        """
        self.counter = 0
        self.alphabet = list(string.ascii_uppercase)

    def generate_name(self):
        """
        Generates the next unique name in the sequence.

        Returns:
            str: The next name in the sequence. If the counter is less than the length of the alphabet, 
                 it returns the corresponding letter in the alphabet. Once the alphabet is exhausted, 
                 it generates repeated names like "AA", "BB", etc.
        """
        if self.counter < len(self.alphabet):
            name = self.alphabet[self.counter]
        else:
            # When the counter exceeds the alphabet length, create a sequence like "AA", "BB", etc.
            repeat = self.counter // len(self.alphabet) + 1
            index = self.counter % len(self.alphabet)
            name = self.alphabet[index] * repeat
        self.counter += 1
        return name
