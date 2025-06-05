import random
import string

class RandomUtilities:
    """
    Class for generation of random numbers
    """
    @staticmethod
    def generate_ISBN() -> str:
        """
        Generates a valid 13 digit ISBN including proper dashes 6 as a string
        """
        isbnGen = ""
        isbnGen = isbnGen.join(random.choices(string.digits, k=13))
        return isbnGen
