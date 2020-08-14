Trying out different design patterns in Python to be able to apply at work.

* Strategy pattern (strategy_pattern.py, strategy_pattern_2.py):
Trying out the strategy pattern, useful when you want to abstract away
business logic without extending classes. It uses an interface which sets
a strategy. The strategy is an abstract class with concrete inherited
implementations.

Useful when:
- you have many algorithms that differ in implementation details only (i.e. avoiding many if-else statements)
- you want to switch strategies at runtime
- you want to provide a clean interface to clients

Not so useful:
- you have only 2 or so algorithms, it adds a lot of bloat then for nothing.
- you are not expected to change the strategy much, especially not at runtime.

Alternatively one can simply provide the abstract base class and it's implementations
and don't use the context so that we still have a a unified client-facing framework
but no code bloat (useful in my case with few algorithm implementations and us being
our own clients with no strategy changes at runtime).
