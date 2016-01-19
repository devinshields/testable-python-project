
from nose.tools import assert_raises

import amazmodule


def test_string_repeater():
    input = 'hello'
    ouput = amazmodule.string_repeater(input)
    assert ouput == 'hellohello'

def test_string_repeater_wrong_type():
    assert_raises(TypeError, amazmodule.string_repeater, 3)

def test_string_repeater_too_short():
    assert_raises(ValueError, amazmodule.string_repeater, '')
