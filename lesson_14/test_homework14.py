import unittest
from homework_14 import SiteUser
from lesson_14pt2 import Money

class TestHomework14(unittest.TestCase):
    def test_positive_case(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
        self.assertTrue(user1==user2)

    def test_negative_same_object_case(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertFalse(user1==user2)
    
    def test_negative_dif_objects_case(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = Money(1)
        self.assertFalse(user1==user2)
    
    def test_negative_dif_types_case(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", 1)
        self.assertFalse(user1==user2)

if __name__ == "__main__":
    unittest.main(verbosity=2)