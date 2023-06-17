import unittest
from gradescope_utils.autograder_utils.decorators import *
import os
import numpy as np
from lightpuzzle import *
import json

from datetime import datetime


class TestLightPuzzle(unittest.TestCase):
    @weight(100)
    def test_grover(self):

        f = open("submission_metadata.json")
        data = json.load(f)
        if 'previous_submissions' in data:
            now = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
            previous_data = data['previous_submissions']
            
            if len(previous_data)>0:
                previous_subs = previous_data[-1]
                # previous = next((i for i in reversed(previous_subs) if "hours" in i['output']), None)
                previous = previous_subs['submission_time']
                previous_time = datetime.strptime(previous, "%Y-%m-%dT%H:%M:%S.%f%z")
                gap = (now-previous_time).total_seconds()
                hour = gap/3600
                if hour < 11.5:
                    self.assertTrue(False, msg=f"You can try the test once per 12 hours, your last submission is {hour:.2f} hours ago")

        n=10
        test=[[0, 1, 1, 1, 0, 0, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 1, 0, 1, 1, 1, 0],
              [0, 1, 1, 0, 1, 1, 0, 1, 1]
              ]
        solutions=['101110000', '000011011', '100110000', '111001111']
        for i in range(len(test)):
            solution = light_out_grover(test[i],17)
            result = solutions[i]
            self.assertTrue(result==solution, msg=f"Your program is incorrect when the input is {test[i]}")


if __name__ == '__main__':
    unittest.main()