
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import numpy as np


suite = unittest.defaultTestLoader.discover('.')
with open('/autograder/results/results.json', 'w') as f:
    JSONTestRunner(visibility='visible', stream=f).run(suite)

