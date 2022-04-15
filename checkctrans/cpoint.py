from math import exp

class Cpoint:
    """А class describing the parameters of a power grid point"""
    
    __ANG_FREQ = 314
    
    def __init__(
                 self, name:str, active_resist:float, reactive_resist:float, 
                 short_circ_curr:int, oper_curr:float):
        self._name = name
        self._active_resist = active_resist
        self._reactive_resist = reactive_resist
        self._short_circ_curr = short_circ_curr
        self._oper_curr = oper_curr
        self.__transit_time_const = (
                self._reactive_resist/
                (self.__ANG_FREQ * self._active_resist))
        self.__impact_coeff = 1 + exp(-0.01/self.__transit_time_const)
        self.__shock_short_curr = (
                                   pow(2, 0.5) * self.__impact_coeff
                                   * self._short_circ_curr)

    def get_jintegr(self, time_setpoint:float)->float:
        """Return calculated value of the joule integral 
        for a power grid point.
        Args:
            time_setpoint (float): Short-circuit current flow time 
            (the time of setting the maximum current protection time)
        Returns:
            Float
        """
        return (
                pow(self._short_circ_curr, 2) 
                * (time_setpoint + self.__transit_time_const))