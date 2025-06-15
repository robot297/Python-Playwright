class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[name="user-name"]')
        self.password_input = page.locator('input[name="password"]')
        self.submit_button = page.locator('input[name="login-button"]')

    def send_username(self, username):
        self.username_input.fill(username)

    def send_password(self, password):
        self.password_input.fill(password)

    def login_click(self):
        self.submit_button.click()
