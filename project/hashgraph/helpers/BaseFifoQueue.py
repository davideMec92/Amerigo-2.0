from typing import TypeVar, List, Generic

T = TypeVar("T")


class BaseFifoQueue(Generic[T]):
    def __init__(self):
        self.elementsList: list[T] = []

    def put(self, element: T):
        self.elementsList.append(element)

    def get(self) -> T:
        return self.elementsList.pop(0) if self.elementsList is not None else None

    def peek(self) -> T:
        return self.elementsList[0] if self.elementsList is not None else None

    def isEmpty(self) -> bool:
        return not self.elementsList

    def size(self) -> int:
        return len(self.elementsList)
