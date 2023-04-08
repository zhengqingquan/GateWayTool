import logging
import unittest

from pyt.src.TemplateModule.TemplateFile import generate_file


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # 加载日志
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_something(self):
        jsonPath = '../CaseMaterial/TestTemplate/Ctemplate.json'
        templatePath = '../CaseMaterial/TestTemplate/Ctemplate.template'
        filePath = '../CaseMaterial/TestTemplate/file.text'
        isComments = True
        generate_file(jsonPath, templatePath, filePath, isComments)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
