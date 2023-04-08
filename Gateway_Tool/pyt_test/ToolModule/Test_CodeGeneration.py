import logging
import unittest

from pyt.src.ToolModule.CodeGeneration import structCode


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_structCode(self):
        structName = 'structName'
        context = '\tstruct context\n'
        logging.info('\n' + structCode(structName, context, isTypedef=True))
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
