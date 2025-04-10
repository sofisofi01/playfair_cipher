import unittest
from playfair_cipher import PlayfairCipher

class TestPlayfairCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher("PLAYFAIREXAMPLE")
    
    def test_matrix_creation(self):
        expected_matrix = [
            ['P', 'L', 'A', 'Y', 'F'],
            ['I', 'R', 'E', 'X', 'M'],
            ['B', 'C', 'D', 'G', 'H'],
            ['K', 'N', 'O', 'Q', 'S'],
            ['T', 'U', 'V', 'W', 'Z']
        ]
        self.assertEqual(self.cipher.matrix, expected_matrix)
    
    def test_encrypt(self):
        test_cases = [
            ("HELLOWORLD", "DMYRANVQCRGE"),
            ("HIDETHEGOLD", "BMODZBXDNAGE"),
            ("TEST", "VIKZ"),
            ("ATTACKATDAWN", "PVVPBNPVOEUQ"),
            ("JAVA", "EPAE"),
            ("A", "YE"),
            ("SHORT", "ZSNEWI")                     
        ]
        
        for plaintext, expected in test_cases:
            with self.subTest(plaintext=plaintext):
                self.assertEqual(self.cipher.encrypt(plaintext), expected)
    
    def test_decrypt(self):
        test_cases = [
            ("DMYRANVQCRGE", "HELXLOWORLD"),
            ("BMODZBXDNAGE", "HIDETHEGOLD"),
            ("VIKZ", "TEST"),
            ("PVVPBNPVOEUQ", "ATACKATDAWN"),
            ("EPAE", "IAVA"),
            ("YE", "A")              
        ]
        
        for ciphertext, expected in test_cases:
            with self.subTest(ciphertext=ciphertext):
                self.assertEqual(self.cipher.decrypt(ciphertext), expected)
    
    def test_special_cases(self):
        self.assertEqual(self.cipher.encrypt("Hello World"), "DMYRANVQCRGE")
        self.assertEqual(self.cipher.decrypt("DMYRANVQCRGE"), "HELXLOWORLD")
        
        with self.assertRaises(ValueError):
            self.cipher.encrypt("HELLO123WORLD!")
        self.assertEqual(self.cipher.decrypt("DMYRANVQCRGE"), "HELXLOWORLD")
    
    def test_key_variations(self):
        test_cases = [
            ("MONARCHY", "HELLOWORLD", "CFSUPMVNMTBZ"),
            ("CRYPTOGRAPHY", "TESTMESSAGE", "RKZBVMQZNBEM"),
            ("EXAMPLE", "SHORT", "QKQSQP")
        ]
        
        for key, plaintext, expected in test_cases:
            with self.subTest(key=key, plaintext=plaintext):
                cipher = PlayfairCipher(key)
                self.assertEqual(cipher.encrypt(plaintext), expected)

if __name__ == "__main__":
    unittest.main()