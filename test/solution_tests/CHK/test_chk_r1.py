from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout('AABCB') == 165
        assert checkout_solution.checkout('') == 0
