import filecmp
import tempfile
import os
import sys
import unittest

unittestDir = os.path.dirname(os.path.realpath(__file__))
scriptDir = os.path.abspath(os.path.join(unittestDir, ".."))
sys.path += [scriptDir]

import rmi2mid

SAMPLE_RMI = os.path.join(unittestDir, "fur_Elise.rmi")
SAMPLE_MID = os.path.join(unittestDir, "fur_Elise_WoO59.mid")


class TestRmi2mid(unittest.TestCase):
    def test_rmi2mid(self):
        (outhdr, outfile) = tempfile.mkstemp(suffix=".mid")
        os.close(outhdr)
        try:
            rmi2mid.rmi2mid(SAMPLE_RMI, outfile)
            self.assertTrue(filecmp.cmp(SAMPLE_MID, outfile))
        finally:
            os.remove(outfile)


if __name__ == '__main__':
    unittest.main()
