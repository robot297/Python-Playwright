class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[name="user-name"]')
        self.password_input = page.locator('input[name="password"]')
        self.submit_button = page.locator('button[type="submit"]')

    async def send_username(self, username):
        await self.username_input.fill(username)
        await self.submit_button.click()

    async def send_password(self, password):
        await self.password_input.fill(password)

    async def login_click(self):
        await self.submit_button.click()
