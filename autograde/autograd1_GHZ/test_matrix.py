import unittest
from gradescope_utils.autograder_utils.decorators import *
import os
import numpy as np

import json

from datetime import datetime

class TestGHZ(unittest.TestCase):
    @weight(100)
    def test_ghz(self):
        f = open("submission_metadata.json")
        data = json.load(f)
        if 'previous_submissions' in data:
            previous_data = data['previous_submissions']
            if len(previous_data)<1:
                pass
            else:
                now = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
                previous = previous_data[-1]['submission_time']
                previous_time = datetime.strptime(previous, "%Y-%m-%dT%H:%M:%S.%f%z")
                gap = (now-previous_time).total_seconds()
                hour = gap/3600
                if hour < 11.5:
                    self.assertTrue(False, msg=f"You can try the test once per 12 hours, your last submission is {hour:.2f} hours ago")
        os.system("python3 ghz.py 6 output.csv")
        array = np.loadtxt("output.csv",delimiter=',',dtype=np.complex_)
        answer = np.loadtxt("answer.csv",delimiter=',',dtype=np.complex_)
        initial = np.array([1]+[0 for i in range(2**6-1)])
        distance = np.linalg.norm(array.dot(initial)-answer.dot(initial))
        self.assertTrue(abs(distance)<0.01, "Your circuit does not provide the GHZ state.")


if __name__ == '__main__':
    unittest.main()