from typing import Union


class MyIterator:
    
    def __init__(self, start: Union[int, float], end: Union[int, float],
         step: Union[int, float] = 1, number_of_decimals: int = 1) -> None:

        self.start = start
        self.end = end
        self.step = step
        self.number_of_decimals = number_of_decimals
        self.current_value = start

    def _ckeck_stop_iteration(self) -> None:
        if self.step >= 0:
            if self.current_value >= self.end:
                raise StopIteration
        else:
            if self.current_value <= self.end:
                raise StopIteration

    def __iter__(self):
        return self

    def __next__(self) -> Union[int, float]:
        
        self._ckeck_stop_iteration()

        value = self.current_value
        self.current_value += self.step
        self.current_value = round(self.current_value, self.number_of_decimals)

        return value
