import pytest

from verification_digit_pty.calculators.natural import calculate_verification_digit


class TestCalculateVerificationDigit:

    def testt_errors(self):
        assert calculate_verification_digit('') == ''
        assert calculate_verification_digit('E') == ''

    @pytest.mark.parametrize("input_value, expected_output", [
        ('61302-14-123411', '22'),
        ('1102-85-117211', '95'),
        ('2486589-1-816994', '62'),
        ('1830234-1-710357', '82'),
        ('65219-68-360495', '20'),
        ('41369-85-283456', '73'),
        ('11947-1027-0229562', '71'),
        ('11947-1-0229562', '42'),
        ('64296-75-357434', '00'),
        ('203141-1-17214', '60'),
        ('1075137-1-553125', '18'),
    ])
    def test_juridical(self, input_value, expected_output):
        assert calculate_verification_digit(input_value) == expected_output

    @pytest.mark.parametrize("input_value, expected_output", [
        ('8-442-445', '08'),
        ('PE-10-442', '50'),
        ('N-45-832', '58'),
        ('E-12-342', '10'),
        ('1AV-432-658', '96'),
        ('4PI-234-123', '96'),
    ])
    def test_natural(self, input_value, expected_output):
        assert calculate_verification_digit(input_value) == expected_output
