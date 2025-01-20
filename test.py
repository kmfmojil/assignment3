#/usr/bin/env python
#
# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import subprocess

class TestSolution(unittest.TestCase):
    
    def test_myfind(self):

        result = subprocess.run(['bash', 'myfind.sh'], stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8')

        assert './files1/lorem3.dat\n' in lines
        assert './files2/lorem2.dat\n' in lines
        assert './files1/files3/lorem3.dat\n' not in lines
        assert './files1/files4/lorem3.dat\n' not in lines
        assert './files2/lorem2.dat\n' in lines
        assert './files2/files5/lorem3.dat\n' not in lines
        assert './files2/files6/lorem3.dat\n' not in lines
        

if __name__ == '__main__':
    unittest.main()




