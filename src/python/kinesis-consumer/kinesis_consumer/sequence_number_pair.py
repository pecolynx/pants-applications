from typing import Any


class SequenceNumberPair:
    def __init__(self, sequence_number: int, sub_sequence_number: int) -> None:
        self.sequence_number = sequence_number
        self.sub_sequence_number = sub_sequence_number

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SequenceNumberPair):
            return NotImplemented

        return (
            self.sequence_number == other.sequence_number
            and self.sub_sequence_number == other.sub_sequence_number
        )

    def __lt__(self, other: "SequenceNumberPair") -> bool:
        if self.sequence_number == other.sequence_number:
            return self.sub_sequence_number < other.sub_sequence_number
        return self.sequence_number < other.sequence_number

    def __le__(self, other: "SequenceNumberPair") -> bool:
        return self == other or self < other

    def __gt__(self, other: "SequenceNumberPair") -> bool:
        return not self <= other

    def __ge__(self, other: "SequenceNumberPair") -> bool:
        return not self < other

    def __hash__(self) -> int:
        return hash((self.sequence_number, self.sub_sequence_number))
