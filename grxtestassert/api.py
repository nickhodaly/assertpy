
class ApiMixin(object):

    def is_success(self):
        """
        Asserts that the response status_code is a success [200-299]
        :param response: requests.Response object
        :return:
        """
        self.is_status_code_between(200, 299)
        return self


    def is_redirect(self):
        """
        Asserts that the response status_code is a redirect [300-399]
        :param response: requests.Response object
        :return:
        """
        self.is_status_code_between(300, 399)
        return self



    def is_client_error(self):
        """
        Asserts that the response status_code is a client error [400-499]
        :param response: requests.Response object
        :return:
        """
        self.is_status_code_between(400, 499)
        return self


    def is_server_error(self):
        """
        Asserts that the response status_code is a server error [500-599]
        :param response: requests.Response object
        :return:
        """
        self.is_status_code_between(500, 599)
        return self



    def is_status_code(self, expected_status):
        """
        Asserts that a requests response status code matches the expected_status
        :param response: requests.Response object
        :param expected_status: Expected HTTP Status Integer code from the Response object
        :return:
        """
        assert self.val.status_code == expected_status, (
            f"The response status code did not match the expected value."
            f" Expected: {expected_status} | Actual: {self.val.status_code}"
        )
        return self


    def is_status_code_between(self, start: int, end: int):
        """
        Asserts that the Response object status_code is between start and end (inclusive)
        :param response: requests.Response object
        :param start: Low range value (inclusive)
        :param end: High range value (inclusive)
        :return:
        """
        assert start <= self.val.status_code <= end, (
            f"The response status code was not between the expected values."
            f" Expected: {start}-{end} | Actual: {self.val.status_code}"
            f" | {self.val.request.method} Request: {self.val.request.url}"
        )
        return self

    def does_response_contain(self, expected_content):
        """
        Asserts that the response JSON object contains the expected data
        :param response: requests.Response object
        :param expected_content:
        :return:
        """
        assert (
            expected_content in self.val.json()
        ), f'message: Expected - {expected_content} not in {self.val.json()}'
        return self


    def is_response_json(self, expected_json):
        """
        Asserts that the response JSON object matches the exepcted_json exactly
        :param response: requests.Response object
        :param expected_json:
        :return:
        """
        assert self.val.json() == expected_json, (
            f"The response content did not match the expected JSON."
        )
        return self
