import unittest
from logger import logger
from homework_11 import log_event


class TestHomework11(unittest.TestCase):
    "Positive test"
    def test_log_event_positive_login(self):
        log_event("Padalka", "success")
    
    "Failed login"
    def test_log_event_negative_login(self):
        log_event("Hello", "failed")
        
    "Expired login"
    def test_log_event_expired_login(self):
        log_event("Padalka1", "expired")
        
if __name__ == "__main__":
    unittest.main(verbosity=2) 