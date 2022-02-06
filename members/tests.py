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


def create_member(
    f_name="test_f_name",
    l_name="test_l_name",
    email="test@test.com",
    phone_number="3535351234",
    role="regular",
):
    """
    Creates a member with the given details
    """
    return Member.objects.create(
        f_name=f_name, l_name=l_name, email=email, phone_number=phone_number, role=role
    )


class MemberListViewTests(TestCase):
    def test_no_members(self):
        response = self.client.get(reverse("members-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have 0 team members.")
        self.assertQuerysetEqual(response.context["members"], [])

    def test_admin_member(self):
        member = create_member(role="Admin")
        response = self.client.get(reverse("members-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "admin")
        self.assertQuerysetEqual(response.context["members"], [member])

    def test_no_admin_member(self):
        member = create_member(role="Regular")
        response = self.client.get(reverse("members-list"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "admin")
        self.assertQuerysetEqual(response.context["members"], [member])

    def test_one_member(self):
        member = create_member(role="Regular")
        response = self.client.get(reverse("members-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have 1 team member.")
        self.assertQuerysetEqual(response.context["members"], [member])
