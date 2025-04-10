class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper().replace("J", "I")
        self.matrix = self._create_matrix()
    
    def _create_matrix(self):
        key_chars = []
        for char in self.key:
            if char not in key_chars and char.isalpha():
                key_chars.append(char)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in key_chars:
                key_chars.append(char)
        
        matrix = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(key_chars[i*5 + j])
            matrix.append(row)
        return matrix
    
    def _prepare_text(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        i = 0
        prepared = []
        while i < len(text):
            if i == len(text) - 1:
                prepared.append(text[i] + "X")
                i += 1
            elif text[i] == text[i+1]:
                prepared.append(text[i] + "X")
                i += 1
            else:
                prepared.append(text[i] + text[i+1])
                i += 2
        return prepared
    
    def _find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return (i, j)
        raise ValueError(f"Символ {char} не найден в матрице")
    
    def encrypt(self, plaintext):
        prepared = self._prepare_text(plaintext)
        ciphertext = []
        
        for pair in prepared:
            a, b = pair[0], pair[1]
            row_a, col_a = self._find_position(a)
            row_b, col_b = self._find_position(b)
            
            if row_a == row_b:
                ciphertext.append(self.matrix[row_a][(col_a + 1) % 5] + self.matrix[row_b][(col_b + 1) % 5])
            elif col_a == col_b:
                ciphertext.append(self.matrix[(row_a + 1) % 5][col_a] + self.matrix[(row_b + 1) % 5][col_b])
            else:
                ciphertext.append(self.matrix[row_a][col_b] + self.matrix[row_b][col_a])
        
        return "".join(ciphertext)
    
    def decrypt(self, ciphertext):
        prepared = self._prepare_text(ciphertext)
        plaintext = []
        
        for pair in prepared:
            a, b = pair[0], pair[1]
            row_a, col_a = self._find_position(a)
            row_b, col_b = self._find_position(b)
            
            if row_a == row_b:
                plaintext.append(self.matrix[row_a][(col_a - 1) % 5] + self.matrix[row_b][(col_b - 1) % 5])
            elif col_a == col_b:
                plaintext.append(self.matrix[(row_a - 1) % 5][col_a] + self.matrix[(row_b - 1) % 5][col_b])
            else:
                plaintext.append(self.matrix[row_a][col_b] + self.matrix[row_b][col_a])
        decrypted = "".join(plaintext)
        if decrypted.endswith("X"):
            decrypted = decrypted[:-1]
        i = 0
        final = []
        while i < len(decrypted):
            if i < len(decrypted) - 1 and decrypted[i] == decrypted[i+1]:
                final.append(decrypted[i])
                i += 2
            else:
                final.append(decrypted[i])
                i += 1
        
        return "".join(final)

def main():
    print("Шифр Плейфера")
    print("=============")
    
    # Ввод ключа
    key = input("Введите ключ (только буквы): ")
    cipher = PlayfairCipher(key)
    
    while True:
        print("\nМеню:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Показать матрицу шифрования")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            plaintext = input("Введите текст для шифрования: ")
            encrypted = cipher.encrypt(plaintext)
            print(f"Зашифрованный текст: {encrypted}")
        elif choice == "2":
            ciphertext = input("Введите текст для дешифрования: ")
            decrypted = cipher.decrypt(ciphertext)
            print(f"Расшифрованный текст: {decrypted}")
        elif choice == "3":
            print("Матрица шифрования:")
            for row in cipher.matrix:
                print(" ".join(row))
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()