from typing import TypeVar, Generic, List

T = TypeVar("T")


class FifoQueue(Generic[T]):

    def __init__(self) -> None:
        self.elementsList: List[T] = []

    def push(self, element: T) -> None:
        self.elementsList.append(element)

    def pop(self) -> T:
        return self.elementsList.pop(0) if self.isEmpty() is False else None

    def peek(self) -> T:
        return self.elementsList[0] if self.isEmpty() is False else None

    def isEmpty(self) -> bool:
        return not self.elementsList

    def size(self) -> int:
        return len(self.elementsList)

    def remove(self) -> None:
        if self.isEmpty() is False:
            self.elementsList.pop(0)
