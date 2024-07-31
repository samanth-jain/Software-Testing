import subprocess

def run_tests():
    try:
        print("Running user registration test...")
        subprocess.run(["python", "Tests/test_user_registration.py"], check=True)

        print("Running product search and details test...")
        subprocess.run(["python", "-m", "unittest", "Tests/ecom_project.py"], check=True)

        print("All tests executed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Test execution failed: {str(e)}")

if __name__ == "__main__":
    run_tests()
