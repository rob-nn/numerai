import unittest
import numpy as np
import read
import model

class TestRead(unittest.TestCase):
    def setUp(self): 
        self._data_set, self._categories = read.get_data_set()

    def tearDown(self): pass

    def test_data_readed(self):
        data_set = self._data_set
        
        first_line = np.array([
            134182390,
            97300587,
            135824563,
            90767607,
            87687197,
            65148427,
            109834029,
            131613166,
            135533479,
            92106582,
            98111205,
            87052852
            ,66216076,
            121781929,
            1,
            0,
            1])
        self.assertTrue(np.all(data_set[0] == first_line))
        self.assertTrue(self._categories["c1_23"])

    def test_model(self):
        data_set = self._data_set
        features = [0, 1]
        ann = model.generate_model(data_set, 5, 5, features)
        self.assertEqual(len(ann.signal_configuration), len(features))


        mid = data_set.shape[0] / 2
        model.train_ann(ann, data_set[:mid,:], 10, features)

        e = model.fire_ann(ann, data_set[mid:,:], features)
        print e



def main():
    unittest.main()

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCmac)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    main()
