// This code is part of Qiskit.
//
// (C) Copyright IBM 2025
//
// This code is licensed under the Apache License, Version 2.0. You may
// obtain a copy of this license in the LICENSE.txt file in the root directory
// of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
//
// Any modifications or derivative works of this code must retain this
// copyright notice, and modified files need to carry a notice indicating
// that they have been altered from the originals.

#[cfg(feature = "python")]
use pyo3::prelude::*;
use pyo3_stub_gen::{define_stub_info_gatherer, derive::*};

/// A Target that contains the constraints(supported instructions, properties etc.) of a particular quantum device
#[derive(Debug, Clone, PartialEq)]
#[gen_stub_pyclass]
#[cfg_attr(feature = "python", pyclass(get_all))]
pub struct Target {
    /// Serialized data
    pub value: String,
}

define_stub_info_gatherer!(stub_info);
