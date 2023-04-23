import unittest
from webspy import core

class TestWebSpy(unittest.TestCase):
    def test_check_href_title(self):
        # Test the check_href_title function
        url = "https://google.com"
        terms = ["google"]
        result = core.check_href_title(url, terms)
        self.assertEqual(result, "https://google.com")

    def test_send_email_with_yagmail(self):
        # TODO: Test the send_email_with_yagmail function
        # Use a mock object to test this function without actually sending an email
        pass

if __name__ == "__main__":
    unittest.main()