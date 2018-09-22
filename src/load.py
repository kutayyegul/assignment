import unittest
loader = unittest.TestLoader()
start_dir = 'Test'
suite = loader.discover(start_dir)
runner = unittest.TextTestRunner()
print "-------------------- Starting -------------------"
print "------------------ %s Test Case ------------------" % suite.countTestCases()
runner.run(suite)