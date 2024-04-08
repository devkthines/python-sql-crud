# test_advanced_user_operations.py

import unittest
from advanced_user_operations import create_user_with_profile, retrieve_users_by_criteria, update_user_profile, delete_users_by_criteria

class TestAdvancedUserOperations(unittest.TestCase):
    def test_create_user(self):
        create_user_with_profile("test_user", "test@example.com", 25, "male", "Test Address")
        users = retrieve_users_by_criteria("username = 'test_user'")
        self.assertEqual(len(users), 1)
        user = users[0]
        self.assertEqual(user[1], "test_user")
        self.assertEqual(user[2], "test@example.com")
        self.assertEqual(user[3], 25)
        self.assertEqual(user[4], "male")
        self.assertEqual(user[5], "Test Address")

    def test_update_user_profile(self):
        create_user_with_profile("test_user", "test@example.com", 25, "male", "Test Address")
        update_user_profile(1, age=30, address="Updated Address")
        users = retrieve_users_by_criteria("username = 'test_user'")
        user = users[0]
        self.assertEqual(user[3], 30)
        self.assertEqual(user[5], "Updated Address")

    def test_delete_users(self):
        create_user_with_profile("test_user1", "test1@example.com")
        create_user_with_profile("test_user2", "test2@example.com")
        create_user_with_profile("test_user3", "test3@example.com")
        delete_users_by_criteria("username LIKE 'test_user%'")
        users = retrieve_users_by_criteria("1=1")
        self.assertEqual(len(users), 0)

if __name__ == '__main__':
    unittest.main()
