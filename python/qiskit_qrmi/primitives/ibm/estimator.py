# This code is part of Qiskit.
#
# (C) Copyright 2025 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""EstimatorV2 Primitive implementation with IBM QRMI"""
# pylint: disable=no-name-in-module
from qiskit_qrmi import QuantumResource
from qiskit_qrmi.primitives import QRMIBaseEstimatorV2


class EstimatorV2(QRMIBaseEstimatorV2):
    """EstimatorV2 for QRMI"""

    def __init__(
        self,
        qrmi: QuantumResource,
        *,
        options: dict | None = None,
    ) -> None:
        super().__init__(qrmi, options=options)
