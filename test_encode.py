import unittest
import subprocess

class TestURLMethods(unittest.TestCase):

    def test_url_encode_argument(self):
        result = subprocess.run(["encode.py", "-u", "?foo&bar"], capture_output=True)
        self.assertEqual("%3Ffoo%26bar", result.stdout.decode().strip())

    def test_url_encode_pipe(self):
        echo_p = subprocess.Popen(
            ["echo", "?foo&bar"],
            stdout=subprocess.PIPE
        )
        encode_p = subprocess.Popen(
            ["encode.py", "-u"],
            stdin=echo_p.stdout,
            stdout=subprocess.PIPE
        )
        echo_p.stdout.close()
        echo_p.kill()
        out, err = encode_p.communicate()
        self.assertEqual("%3Ffoo%26bar", out.decode().strip())

    def test_url_decode(self):
        result = subprocess.run(["encode.py", "-u", "-d", "%3Ffoo%26bar"], capture_output=True)
        self.assertEqual("?foo&bar", result.stdout.decode().strip())

    def test_url_encode_safe(self):
        result = subprocess.run(["encode.py", "-u", "-s", "/?foo&bar"], capture_output=True)
        self.assertEqual("%2F%3Ffoo%26bar", result.stdout.decode().strip())

class TestDecimalMethods(unittest.TestCase):

    def test_decimal_encode(self):
        result = subprocess.run(["encode.py", "--decimal", "foo"], capture_output=True)
        self.assertEqual("102 111 111", result.stdout.decode().strip())

    def test_decimal_decode(self):
        result = subprocess.run(["encode.py", "--decimal", "-d", "102 111 111"], capture_output=True)
        self.assertEqual("foo", result.stdout.decode().strip())


if __name__ == "__main__":
    unittest.main()
