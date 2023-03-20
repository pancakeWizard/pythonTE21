# a = float(input("Enter a number. "))
# b = float(input("Enter a number to divide by. "))

# try:
#     print(f"The answer is {a/b}.")
# except:
#     if b == 0:
#         raise
#         print("This did not work.")
# else: 
#     print("You successfully used the divistion feature in Python.")
# finally:
#     print("Thank yout for playing.")

import unittest
a = 3
b = 5

class Test__53a_UnitTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(3+5, a+b)

    def test_greater(self):
        self.assertTrue(a+b > 3+4)

if __name__ == '__main__':
    unittest.main()