from lib.solutions.CHK import checkout_solution


class CheckTest:
    def test_check(self):
        assert checkout_solution.checkout('AABCB') == 165
        assert checkout_solution.checkout('AABCBE') == -1
