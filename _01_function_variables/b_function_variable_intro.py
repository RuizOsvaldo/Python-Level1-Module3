"""
Introduction to storing functions in variables
"""
import unittest


def surprise():
    return 'SURPRISE!'

# TODO 1) Change what is assigned into the func_1 variable so test_1 will pass
func_1 = surprise

# TODO 2) Change the return statement below so that test_2 will pass
def pizza_surprise():
    return "SURPRISE, here's a pizza!"

func_2 = pizza_surprise

# TODO 3) Implement the birthday_surprise function so that test_3 will pass
def birthday_surprise(years_old):
    birthday_wish = "SURPRISE, Happy "
    birthday_wish_second_half = " birthday!!!"
    years_old = str(years_old)
    if years_old == '1':
        birthday_wish += years_old +"st" + birthday_wish_second_half 
    elif years_old == '2':
        birthday_wish += years_old +"nd" + birthday_wish_second_half 
    elif years_old == '3':
        birthday_wish += years_old +"rd" + birthday_wish_second_half 
    else:
        birthday_wish += years_old +"th" + birthday_wish_second_half
    return birthday_wish

func_3 = birthday_surprise
# TODO 4) Implement the surprise_guests function so that test_3 will pass
#  *HINT* You will have to add input parameters to the function
def surprise_guests(message, guests):
    surprise_guests = ''
    for guest in guests:
        surprise_guests += guest + ' says '+ message() +'\n'
    return surprise_guests

# ================== DO NOT MODIFY THE CODE BELOW ============================

class WriteClassesTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual('SURPRISE!', func_1())

    def test_2(self):
        func_2 = pizza_surprise
        self.assertEqual("SURPRISE, here's a pizza!", func_2())

    def test_3(self):
        func_3 = birthday_surprise
        self.assertEqual('SURPRISE, Happy 1st birthday!!!', func_3(1))
        self.assertEqual('SURPRISE, Happy 2nd birthday!!!', func_3(2))
        self.assertEqual('SURPRISE, Happy 3rd birthday!!!', func_3(3))
        self.assertEqual('SURPRISE, Happy 38th birthday!!!', func_3(38))

    def test_4(self):
        guests = ['Jerry', 'Summer', 'Yusef']
        expected_message =  guests[0] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[1] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[2] + ' says ' + 'SURPRISE!\n'
        self.assertEqual(expected_message, surprise_guests(surprise, guests))

        expected_message =  guests[0] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[1] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[2] + ' says ' + "SURPRISE, here's a pizza!\n"
        self.assertEqual(expected_message, surprise_guests(pizza_surprise, guests))

if __name__ == '__main__':
    unittest.main()
