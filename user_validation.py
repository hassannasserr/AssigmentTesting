# user_validation.py
import re
from datetime import datetime


class UserValidation:
    """
    A class for validating user-related inputs like emails, usernames,
    Egyptian phone numbers, and Egyptian national IDs.
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates if the provided email is in a proper format.
        [cite: 26, 27]
        """
        # First, handle the None or empty string cases
        if not email or not isinstance(email, str):
            return False


        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # re.match() checks if the pattern matches from the *start* of the string.
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_username(username: str) -> bool:

        # Handle None or empty string cases
        if not username or not isinstance(username, str):
            return False


        pattern = r"^[a-zA-Z0-9_]{3,20}$"

        return re.match(pattern, username) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """
        Validates Egyptian phone number (11 digits total or 12 if it starts with 20).
        [cite: 34, 35]
        """
        if not phone or not isinstance(phone, str):
            return False


        pattern = r"^(01(0|1|2|5)\d{8})$|^(201(0|1|2|5)\d{8})$"

        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """
        Validates Egyptian national ID (14 digits with valid date and governorate code).
        [cite: 38, 39]
        """
        if not national_id or not isinstance(national_id, str):
            return False


        pattern = r"^(2|3)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-7]\d|8[0-8])\d{5}$"

        if re.match(pattern, national_id) is None:
            return False

      
        try:
            # Extract date parts
            # Century doesn't matter for date validation
            year_str = national_id[1:3]
            month_str = national_id[3:5]
            day_str = national_id[5:7]


            year = int(f"19{year_str}") if national_id[0] == '2' else int(f"20{year_str}")
            month = int(month_str)
            day = int(day_str)

            # This will raise a ValueError for invalid dates (e.g., 30/02/1998)
            datetime(year=year, month=month, day=day)

            return True
        except ValueError:
            # Failed to parse as a real date
            return False