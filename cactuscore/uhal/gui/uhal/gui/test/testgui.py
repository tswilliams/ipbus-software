import unittest

import uhal.gui.guiloader


class TestGuiImports(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_default_on(self):
        print '********** Simple configuration **********'
        g = uhal.gui.guiloader.GuiLoader(test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')
        print


    def test_default_off(self):    
        print '********** Configuration: default=No, guilist=[] **********'
        g = uhal.gui.guiloader.GuiLoader(default='No', test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')
        print


    def test_default_on_custom_one(self):
        print '********** Configuration: default=Yes, guilist=[\'CustomWindow1\'] **********'
        g = uhal.gui.guiloader.GuiLoader(guilist=['CustomWindow1'], test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')
        print


    def test_default_off_custom_one(self):
        print '********** Configuration: default=No, guilist=[\'CustomWindow1\'] **********'
        g = uhal.gui.guiloader.GuiLoader(default='No', guilist=['CustomWindow1'], test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')
        print


    def test_default_on_custom_one_two(self):
        print '********** Configuration: default=Yes, guilist=[\'CustomWindow1\',\'CustomWindow2\']**********'
        g = uhal.gui.guiloader.GuiLoader(guilist=['CustomWindow1','CustomWindow2'], test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')        
        print


    def test_default_off_custom_one_two(self):
        print '********** Configuration: default=No, guilist=[\'CustomWindow1\',\'CustomWindow2\'] **********'
        g = uhal.gui.guiloader.GuiLoader(default='No', guilist=['CustomWindow1','CustomWindow2'], test_mode='Yes')
        self.assertEqual(g.start_test(), 'OK')
        print

    
    def test_default_off_non_existing(self):
        print '********** Configuration: default=No, guilist=[\'NonExistingWindow\'] **********'
        g = uhal.gui.guiloader.GuiLoader(default='No', guilist=['NonExistingWindow'], test_mode='Yes')
        self.assertEqual(g.start_test(), 'FAILED')
        print




def suite():
    suite = unittest.makeSuite(TestGuiImports, 'test')
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')