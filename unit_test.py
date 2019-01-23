import unittest
import get_depth
import get_class_depth
import get_lca


class TaskTest(unittest.TestCase):

    def test_depth(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "key6": {
                        "key7": 9
                    }
                }
            }
        }
        result = get_depth.print_depth(a)
        self.assertEqual(result['key1'], 1)
        self.assertEqual(result['key2'], 1)
        self.assertEqual(result['key3'], 2)
        self.assertEqual(result['key4'], 2)
        self.assertEqual(result['key5'], 3)
        self.assertEqual(result['key6'], 3)
        self.assertEqual(result['key7'], 4)

    def test_class_depth(self):
        result = get_class_depth.print_depth()
        self.assertEqual(result['key1'], 1)
        self.assertEqual(result['key2'], 1)
        self.assertEqual(result['key3'], 2)
        self.assertEqual(result['key4'], 2)
        self.assertEqual(result['key5'], 3)
        self.assertEqual(result['user'], 3)
        self.assertIn(4, result['first_name'])
        self.assertIn(5, result['first_name'])
        self.assertIn(4, result['last_name'])
        self.assertIn(5, result['last_name'])
        self.assertIn(4, result['father'])
        self.assertIn(5, result['father'])

    def test_lca(self):
        result_1 = get_lca.lca(node1=6, node2=7)
        self.assertEqual(result_1, 3)
        result_2 = get_lca.lca(node1=3, node2=7)
        self.assertEqual(result_2, 3)


if __name__ == '__main__':
    unittest.main()


