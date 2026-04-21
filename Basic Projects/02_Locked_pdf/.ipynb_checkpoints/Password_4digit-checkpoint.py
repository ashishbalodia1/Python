# Unlock a 6 digit password
import pikepdf
import tqdm

def try_password(pdf_path, password):
    try:
        with pikepdf.open(pdf_path, password=password):  # Bug 1 Fixed ✅
            print(f"Password found: {password}")
            return True

    except pikepdf.PasswordError:
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def crack_password(pdf_path):
    print("Starting password cracking...")
    for i in tqdm.tqdm(range(1000000), desc="Trying passwords"):  # Bug 3 Fixed ✅
        password = f"{i:06d}"  # 000000 to 999999
        if try_password(pdf_path, password):  # Bug 2 Fixed ✅
            return password

    print("Password not found.")
    return None


if __name__ == "__main__":
    pdf_path = r"C:\Users\ashis\OneDrive\Desktop\01_start\Basic Projects\02_Locked_pdf\.ipynb_checkpoints\SEM6FEE_protected.pdf"
    found_password = crack_password(pdf_path)
    if found_password:
        print(f"Password successfully cracked: {found_password}")
    else:
        print("Failed to crack the password.")