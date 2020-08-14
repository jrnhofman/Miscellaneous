from abc import ABC, abstractmethod

"""
Abstract base class defining abstract methods
"""
class Strategy(ABC):

    @abstractmethod
    def get_table_name(self, **settings):
        pass

    @abstractmethod
    def create_table_statement(self, **settings):
        pass

    @abstractmethod
    def other(self):
        pass

"""
Context with primary function of setting the correct strategy
Mostly boilerplate, doesn't really do much
"""
class TableContext():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_table_name(self, **settings) -> str:
        return self._strategy.get_table_name(**settings)

    def create_table_statement(self, **settings) -> str:
        return self._strategy.create_table_statement(**settings)

    def other(self) -> None:
        return self._strategy.other()

"""
Actual implementations of Strategy class
"""
class NoPartitionStrategy(Strategy):

    def get_table_name(self, **settings) -> str:
        print(settings)
        print("We do logic to handle non-partitioned tables")

        return settings['base_name'] + '_' + settings['date'] + '_slice_' + str(settings['exp_slice'])

    def create_table_statement(self, **settings) -> str:
        return f"CREATE TABLE IF NOT EXISTS {settings['table_name']} (...)"

    def other(self) -> None:
        print("Doing other stuff related to non-partitioned strategy")

class PartitionStrategy(Strategy):

    def get_table_name(self, **settings) -> str:
        print(settings)
        print("We do logic to handle partitioned tables")

        return settings['base_name'] + '_' + settings['date']

    def create_table_statement(self, **settings) -> str:
        return f"""CREATE TABLE IF NOT EXISTS {settings['table_name']} (...)
            PARTITIONED BY {settings['partition_field']}
        """

    def other(self) -> None:
        print("Doing other stuff related to partitioned strategy")


if __name__ == "__main__":

    partition_settings = {'base_name' : 'foo', 'date' : '20200707', 'exp_slice' : 0}

    tc = TableContext(NoPartitionStrategy())

    tn = tc.get_table_name(**partition_settings)
    print("The table name is {}".format(tn))


    # Alternative without using strategy pattern
    is_partitioned = True
    if is_partitioned:
        s = PartitionStrategy()
    else:
        s = NoPartitionStrategy()

    s.get_table_name(**partition_settings)
    print("The table name is {}".format(tn))