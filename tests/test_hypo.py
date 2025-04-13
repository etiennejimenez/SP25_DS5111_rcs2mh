import sys
sys.path.append('.')

import bin.sample_hypo as hypotenuse

def test_hypo():
    assert 5.0 == hypotenuse.hypo(3, 4), "Hypo failed with sides 3.0 and 4.0, expected 5.0"
