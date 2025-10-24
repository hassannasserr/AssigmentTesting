# test_user_validation.py
import unittest
from user_validation import UserValidation


class TestUserValidation(unittest.TestCase):

    # --- 1. Email Validation Tests --- [cite: 49]

    def test_valid_email_returns_true(self):
        # Arrange
        email = "user@example.com"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertTrue(result)

    def test_email_missing_at_symbol_returns_false(self):
        # Arrange
        email = "userexample.com"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    def test_email_missing_domain_returns_false(self):
        # Arrange
        email = "user@"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    def test_email_invalid_tld_returns_false(self):
        # Arrange
        email = "user@mail.c"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    def test_email_with_subdomain_returns_true(self):
        # Arrange
        email = "user@mail.company.com"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertTrue(result)

    def test_email_with_special_chars_returns_true(self):
        # Arrange
        email = "ramy.gomaa21@mail.co"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertTrue(result)

    def test_uppercase_email_returns_true(self):
        # Arrange
        email = "USER@MAIL.COM"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertTrue(result)

    def test_email_with_space_returns_false(self):
        # Arrange
        email = "user name@mail.com"  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    def test_empty_email_returns_false(self):
        # Arrange
        email = ""  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    def test_null_email_returns_false(self):
        # Arrange
        email = None  #
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertFalse(result)

    # --- 2. Username Validation Tests --- [cite: 51]

    def test_valid_username_returns_true(self):
        # Arrange
        username = "ramy_gomaa"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertTrue(result)

    def test_username_too_short_returns_false(self):
        # Arrange
        username = "ab"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    def test_username_too_long_returns_false(self):
        # Arrange
        username = "ramygomaaisaverylongusername"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    def test_username_with_spaces_returns_false(self):
        # Arrange
        username = "ramy gomaa"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    def test_username_with_symbols_returns_false(self):
        # Arrange
        username = "ramy@123"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    def test_username_with_digits_returns_true(self):
        # Note: Test case table conflicts with rules.
        # Following rules, so this should be TRUE.
        # Arrange
        username = "ramy123"  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertTrue(result)

    def test_empty_username_returns_false(self):
        # Arrange
        username = ""  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    def test_null_username_returns_false(self):
        # Arrange
        username = None  #
        # Act
        result = UserValidation.validate_username(username)
        # Assert
        self.assertFalse(result)

    # --- 3. Phone Number Validation Tests --- [cite: 53]

    def test_valid_vodafone_number_returns_true(self):
        # Arrange
        phone = "01012345678"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_valid_orange_number_returns_true(self):
        # Arrange
        phone = "01234567890"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_valid_etisalat_number_returns_true(self):
        # Arrange
        phone = "01198765432"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_valid_we_number_returns_true(self):
        # Arrange
        phone = "01555555555"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_valid_vodafone_with_country_code_returns_true(self):
        # Arrange
        phone = "201012345678"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_valid_orange_with_country_code_returns_true(self):
        # Arrange
        phone = "201234567890"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertTrue(result)

    def test_invalid_phone_prefix_returns_false(self):
        # Arrange
        phone = "01812345678"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    def test_phone_too_short_returns_false(self):
        # Arrange
        phone = "0101234567"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    def test_phone_too_long_returns_false(self):
        # Arrange
        phone = "010123456789"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    def test_phone_contains_chars_returns_false(self):
        # Arrange
        phone = "01012abc678"  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    def test_empty_phone_returns_false(self):
        # Arrange
        phone = ""  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    def test_null_phone_returns_false(self):
        # Arrange
        phone = None  #
        # Act
        result = UserValidation.validate_phone_number(phone)
        # Assert
        self.assertFalse(result)

    # --- 4. National ID Validation Tests --- [cite: 55]

    def test_valid_national_id_returns_true(self):
        # Arrange
        nid = "29812251234567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertTrue(result)

    def test_national_id_too_short_returns_false(self):
        # Arrange
        nid = "2981225123456"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_too_long_returns_false(self):
        # Arrange
        nid = "298122512345678"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_contains_letters_returns_false(self):
        # Arrange
        nid = "2981225AB34567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_century_returns_false(self):
        # Arrange
        nid = "19812251234567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_month_returns_false(self):
        # Arrange
        nid = "29813251234567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_day_returns_false(self):
        # Arrange
        nid = "29812323234567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_day_or_gov_code_returns_false(self):
        # Note: Test case has an invalid day (38)
        # and an invalid governorate (00). My regex catches both.
        # Arrange
        nid = "29812380034567"  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_empty_national_id_returns_false(self):
        # Arrange
        nid = ""  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_null_national_id_returns_false(self):
        # Arrange
        nid = None  #
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_date_feb_30_returns_false(self):
        # This is an extra test to check our datetime logic
        # Arrange
        nid = "29602301234567"  # Feb 30, 1996
        # Act
        result = UserValidation.validate_national_id(nid)
        # Assert
        self.assertFalse(result)


# This block allows you to run the tests from the command line
if __name__ == '__main__':
    unittest.main()