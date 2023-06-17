import unittest
from gradescope_utils.autograder_utils.decorators import *
import os
import numpy as np
from teleportation import *
import json

from datetime import datetime


class TestTeleportation(unittest.TestCase):
    @weight(100)
    def test_teleport(self):

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
        os.system("python3 teleportation.py")
        n=10
        for i in range(n):
            psi,result = teleportation()
            print("psi ", psi)
            print("result ", result)
            self.assertTrue(result.equiv(psi), msg="qubit[2]'s final state does not match the initial state psi")


if __name__ == '__main__':
    unittest.main()