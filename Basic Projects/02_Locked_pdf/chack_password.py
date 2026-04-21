# Password is a combination of digits and numbers
import pikepdf
import tqdm
import itertools
import string

def try_password(pdf_path, password):
    try:
        with pikepdf.open(pdf_path, password=password):
            print(f"\nPassword found: {password}")
            return True
    except pikepdf.PasswordError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def crack_password(pdf_path, min_length=6, max_length=8):
    print("Starting password cracking...")

    # Characters to use — numbers + lowercase + uppercase
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

    for length in range(min_length, max_length + 1):
        print(f"\nTrying length: {length}")
        total = len(characters) ** length

        for combo in tqdm.tqdm(itertools.product(characters, repeat=length), 
                                total=total, desc=f"Length {length}"):
            password = ''.join(combo)
            if try_password(pdf_path, password):
                return password

    print("Password not found.")
    return None


if __name__ == "__main__":
    pdf_path = r"C:\Users\ashis\OneDrive\Desktop\01_start\Basic Projects\02_Locked_pdf\.ipynb_checkpoints\SEM6FEE_protected.pdf"
    found_password = crack_password(pdf_path, min_length=6, max_length=8)
    if found_password:
        print(f"Password successfully cracked: {found_password}")
    else:
        print("Failed to crack the password.")