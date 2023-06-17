import unittest
from gradescope_utils.autograder_utils.decorators import *
import os
import numpy as np
from qutip import *
from qutip_try import integrate2
from spin import integrate
import json


from datetime import datetime


class TestHamil(unittest.TestCase):
    @weight(100)
    def test_hamil(self):

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
                if hour < 0.001:
                    self.assertTrue(False, msg=f"You can try the test once per 12 hours, your last submission is {hour:.2f} hours ago")

        N = 3            # number of spins
        h  = 1.0 * 2 * np.pi * np.ones(N) 
        Jz = 0.1 * 2 * np.pi * np.ones(N)
        Jx = 0.1 * 2 * np.pi * np.ones(N)
        Jy = 0.1 * 2 * np.pi * np.ones(N)

        # intial state, first spin in state |1>, the rest in state |0>
        psi_list = []
        psi_list.append(basis(2,1))
        for n in range(N-1):
            psi_list.append(basis(2,0))
        psi0 = tensor(psi_list)
        point = 5
        tlist = np.linspace(0, 2, point)
        sz_expt = integrate(N, h, Jx, Jy, Jz, psi0, tlist)
        answer = integrate2(N, h, Jx, Jy, Jz, psi0, tlist)
        for i in range(len(answer)):
            distance = np.linalg.norm(sz_expt[i].full()-answer[i].full())
            self.assertTrue(abs(distance)<0.01, "Your Hamiltonian is not correct.")


if __name__ == '__main__':
    unittest.main()