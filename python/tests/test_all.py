import pytest
import qiskit_qrmi


def test_sum_as_string():
    assert qiskit_qrmi.sum_as_string(1, 1) == "2"
