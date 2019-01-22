import unittest,sys

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith('mac'),'require mac')
    def test_zformat(self):
        # Tests that work for only a certain version of the library.
        # self.assertEqual("1","2")
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)