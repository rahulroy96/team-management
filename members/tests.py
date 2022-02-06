from django.test import TestCase
from django.urls import reverse
from .models import Member

# test cases which tests the MemberModel
class MemberModelTests(TestCase):
    def test_is_admin_with_admin_member(self):
        """
        is_admin returns true for members who are admins
        """
        admin_member = Member(
            f_name="test_f_name",
            l_name="test_l_name",
            email="test@test.com",
            phone_number="3234567890",
            role="Admin",
        )
        self.assertIs(admin_member.is_admin(), True)

    def test_is_admin_with_regular_member(self):
        """
        is_admin returns false for members who are not admin
        """
        admin_member = Member(
            f_name="test_f_name",
            l_name="test_l_name",
            email="test@test.com",
            phone_number="3234567890",
            role="Regular",
        )
        self.assertIs(admin_member.is_admin(), False)


