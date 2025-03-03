import unittest
from homework_11 import log_event

TESTDATA_FILENAME = "/Users/Oleksandra/aqa_090125/login_system.log"

class TestHomework11(unittest.TestCase):
    "Positive test"
    def test_log_event_positive_login(self):
        expected_result_status = "success"
        expected_result_name = "Padalka"
        expected_log_output = f"Login event - Username: {expected_result_name}, Status: {expected_result_status}"
        log_event(expected_result_name, expected_result_status)
        self.list_from_logs = list(open(TESTDATA_FILENAME))
        index_of_last_item = len(self.list_from_logs)-1
        actual_log_output = self.list_from_logs[index_of_last_item]
        self.assertIn(expected_log_output, actual_log_output)
        
    "Failed login"
    def test_log_event_negative_login(self):
        expected_result_status = "failed"
        expected_result_name = "Hello"
        expected_log_output = f"Login event - Username: {expected_result_name}, Status: {expected_result_status}"
        log_event(expected_result_name, expected_result_status)
        self.list_from_logs = list(open(TESTDATA_FILENAME))
        index_of_last_item = len(self.list_from_logs)-1
        actual_log_output = self.list_from_logs[index_of_last_item]
        self.assertIn(expected_log_output, actual_log_output)
        
    "Expired login"
    def test_log_event_expired_login(self):
        expected_result_status = "expired"
        expected_result_name = "Petrov"
        expected_log_output = f"Login event - Username: {expected_result_name}, Status: {expected_result_status}"
        log_event(expected_result_name, expected_result_status)
        self.list_from_logs = list(open(TESTDATA_FILENAME))
        index_of_last_item = len(self.list_from_logs)-1
        actual_log_output = self.list_from_logs[index_of_last_item]
        self.assertIn(expected_log_output, actual_log_output)
        
        
if __name__ == "__main__":
    unittest.main(verbosity=2) 