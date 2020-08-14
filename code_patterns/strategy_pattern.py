from abc import ABC, abstractmethod

"""
Abstract base class defining abstract methods
"""
class Strategy(ABC):

    @abstractmethod
    def update(self, **settings):
        pass

"""
Context with primary function of setting the correct strategy
Mostly boilerplate, doesn't really do much
"""
class UpdatorContext():

    def __init__(self, strategy: Strategy) -> None:

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def update(self, **settings) -> None:

        return self._strategy.update(**settings)

"""
Actual implementations of Strategy class
"""
class SimulationStrategy(Strategy):

    def update(self, **settings) -> None:
        print(settings)
        print("We do logic to handle simulations")

class AlgoStrategy(Strategy):

    def update(self, **settings) -> None:
        print(settings)
        print("We do logic to handle the algo")


if __name__ == "__main__":

    updator = UpdatorContext(SimulationStrategy())

    updator.update(foo=1, alpha=2)


    updator = UpdatorContext(AlgoStrategy())

    updator.update(foo=3, alpha=4)