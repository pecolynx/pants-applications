from kinesis_consumer.domain.sequence_number import SequenceNumber


def test_sequence_number_pair():
    sequence_number_pair = SequenceNumber(123, 456)
    assert sequence_number_pair.sequence_number == 123
    assert sequence_number_pair.sub_sequence_number == 456


def test_sequence_number_pair_equality():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 456)
    assert sequence_number_pair_1 == sequence_number_pair_2


def test_sequence_number_pair_inequality():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 457)
    assert sequence_number_pair_1 != sequence_number_pair_2

    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(124, 456)
    assert sequence_number_pair_1 != sequence_number_pair_2


def test_sequence_number_pair_less_than():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 457)
    assert sequence_number_pair_1 < sequence_number_pair_2


def test_sequence_number_pair_less_than_equal():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 456)
    assert sequence_number_pair_1 <= sequence_number_pair_2


def test_sequence_number_pair_greater_than():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 455)
    assert sequence_number_pair_1 > sequence_number_pair_2


def test_sequence_number_pair_greater_than_equal():
    sequence_number_pair_1 = SequenceNumber(123, 456)
    sequence_number_pair_2 = SequenceNumber(123, 456)
    assert sequence_number_pair_1 >= sequence_number_pair_2
