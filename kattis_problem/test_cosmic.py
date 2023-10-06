import unittest
import cosmic


class TestCosmic(unittest.TestCase):

    def test_calc_mean1(self) -> None:
        tmp = [123, 769, 903, 645]
        tmp_total = 4
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 610
        self.assertEqual(actual_ans, expected_ans)

    def test_calc_mean2(self) -> None:
        tmp = [213, 725, 844, 564, 389, 127, 1345, 812, 987, 357, 908]
        tmp_total = 11
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 661
        self.assertEqual(actual_ans, expected_ans)

    def test_calc_mean3(self) -> None:
        tmp = [321, 345]
        tmp_total = 2
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 333
        self.assertEqual(actual_ans, expected_ans)

    def test_calc_mean4(self) -> None:
        tmp = [123]
        tmp_total = 1
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 123
        self.assertEqual(actual_ans, expected_ans)

    def test_calc_mean5(self) -> None:
        tmp = [123, 769, 903, 645, 874, 932,
               289, 309, 321, 784, 964, 235,
               173, 684, 549, 913, 7323, 1893,
               178, 367, 204, 397, 855, 689, 340]
        tmp_total = 25
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 868
        self.assertEqual(actual_ans, expected_ans)

    def test_calc_mean6(self) -> None:
        tmp = [567, 890, 907, 340, 432]
        tmp_total = 5
        actual_ans = cosmic.calc_mean(tmp_total, tmp)
        expected_ans = 627
        self.assertEqual(actual_ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
