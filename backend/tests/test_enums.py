from account_v2.enums import UserRole


def test_user_role_enum_values():
    """
    Test that UserRole enum contains all expected values with correct string representations.
    This test ensures that the UserRole enum is correctly defined with the expected roles
    and their corresponding string values.
    """
    assert len(UserRole) == 2, "UserRole should have exactly 2 members"
    assert UserRole.USER.value == "user", "USER role should have value 'user'"
    assert UserRole.ADMIN.value == "admin", "ADMIN role should have value 'admin'"

    # Check if all expected roles are present
    expected_roles = {"USER", "ADMIN"}
    actual_roles = set(UserRole.__members__.keys())
    assert actual_roles == expected_roles, f"Expected roles {expected_roles}, but got {actual_roles}"
