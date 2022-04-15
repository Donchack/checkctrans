class Currtrans:
    """The class of the current measuring transformer. 
        The parameters necessary for calculating the damage and accuracy class of the transformer are implemented."""
    
    def __init__(
                 self, name:str, nominal_first_i:int, trans_coeff:int, 
                 term_resist_i_1s:float, eldinam_resist_i:float):
        self._name = name
        self._nominal_first_i = nominal_first_i
        self._trans_coeff = trans_coeff
        self._term_resist_i_1s = term_resist_i_1s
        self._eldinam_resist_i = eldinam_resist_i
    
    def get_accept_val_jintegr(self)->float:
        """Return acceptable value of the joule integral 
        for a current transformer.
        Args:
            None
        Returns:
            Float
        """
        return pow(self._term_resist_i_1s * 1000, 2)

