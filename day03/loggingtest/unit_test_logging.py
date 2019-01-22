import logging,unittest

FORMAT = '%(asctime)-15s %(clientip)s %(user)s %(action)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs','action':'test'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)
logging.basicConfig(format=FORMAT,filename = 'log.log',level = logging.INFO)
class TestStringMethods(unittest.TestCase):

    '''
    API实例
    '''
    
    def test_upper(self):
        # d = {'clientip': '192.168.0.1', 'user': 'user01','action':'test'}
        # logger.warning('Protocol problem: %s', 'connection reset', extra=d)
        d = {'clientip': '192.168.0.1', 'user': 'user01','action':'test'}
        logging.warning('Protocol problem: %s',"test case", extra = d)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()


