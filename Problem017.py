# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# e.g. 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

_ones_place_numbers = {
    '1': 3,  # one
    '2': 3,  # two
    '3': 5,  # three
    '4': 4,  # four
    '5': 4,  # five
    '6': 3,  # six
    '7': 5,  # seven
    '8': 5,  # eight
    '9': 4,  # nine
}
_tens_place_numbers = {
    '2': 6,  # twenty
    '3': 6,  # thirty
    '4': 5,  # forty
    '5': 5,  # fifty
    '6': 5,  # sixty
    '7': 7,  # seventy
    '8': 6,  # eighty
    '9': 6,  # ninety
}
_other_numbers = {
    '10': 3,  # ten
    '11': 6,  # eleven
    '12': 6,  # twelve
    '13': 8,  # thirteen
    '14': 8,  # fourteen
    '15': 7,  # fifteen
    '16': 7,  # sixteen
    '17': 9,  # seventeen
    '18': 8,  # eighteen
    '19': 8,  # nineteen
}


def impl(ceiling: int):
    sum_ = 0
    for x in range(1, ceiling):
        if x > 999:
            sum_ += _sum_four_digits(x)
        elif x > 99:
            sum_ += _sum_three_digits(x)
        elif x > 9:
            sum_ += _sum_two_digits(x)
        elif x > 0:
            sum_ += _ones_place_numbers.get(str(x))
    return sum_


def _sum_four_digits(n: int):
    s = str(n)
    sum_ = 0
    if 999 < n < 10000:
        sum_ += _ones_place_numbers.get(s[0])
        sum_ += 8  # thousand
        temp = n % 1000
        if temp != 0:
            if temp > 99:
                sum_ += _sum_three_digits(temp)
            else:
                sum_ += 3  # and
                if temp > 9:
                    sum_ += _sum_two_digits(temp)
                elif temp > 0:
                    sum_ += _ones_place_numbers.get(str(temp))
    return sum_


def _sum_three_digits(n: int):
    s = str(n)
    sum_ = 0
    if 99 < n < 1000:
        sum_ += _ones_place_numbers.get(s[0])
        sum_ += 7  # hundred
        temp = n % 100
        if temp != 0:
            sum_ += 3  # and
            if temp > 9:
                sum_ += _sum_two_digits(temp)
            else:
                sum_ += _ones_place_numbers.get(str(temp))
    return sum_


def _sum_two_digits(n: int):
    s = str(n)
    sum_ = 0
    if 9 < n < 100:
        if n > 19:
            sum_ += _tens_place_numbers.get(s[0])
            if n % 10 != 0:
                sum_ += _ones_place_numbers.get(s[1])
        else:
            sum_ += _other_numbers.get(s)
    return sum_


# def test():
#     assert 19 == impl(6)  # one two three four five
#     assert 6 == _sum_two_digits(20)  # twenty
#     assert 10 == _sum_three_digits(100)  # one hundred
#     assert 16 == _sum_three_digits(101)  # one hundred and one
#     assert 20 == _sum_three_digits(115)  # one hundred and fifteen
#     assert 24 == _sum_three_digits(197)  # one hundred and ninety seven
#     assert 11 == _sum_four_digits(1000)  # one thousand
#     assert 17 == _sum_four_digits(1001)  # one thousand and one


print("answer:", impl(1001))
