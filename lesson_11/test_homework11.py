import unittest
import logger
from homework_11 import log_event


class TestHomework11(unittest.TestCase):
    "Positive test"
    def test_log_event_positive_login(self):
        self.assertTrue(log_event("Padalka", "success"))
    
    "Failed login"
    def test_log_event_negative_login(self):
        self.assertFalse(log_event("Hello", "failed"))
        
    "Expired login"
    def test_log_event_expired_login(self):
        self.assertEqual(log_event("Petrov", "expired"), "Your password is expired")
        
if __name__ == "__main__":
    unittest.main(verbosity=2) 