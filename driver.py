from selenium import webdriver
from config import USER_DATA_DIR,USER_PROFILE

Options = webdriver.ChromeOptions()


Options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
Options.add_argument(f'--profile-directory={USER_PROFILE}')

