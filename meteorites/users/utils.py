from django.contrib.auth import login


class Manager:
    def __init__(self, req, ctx, form, name='form'):
        self.req = req
        self.ctx = ctx
        self.form = form
        self.name = name

    def _binding(self):
        self.ctx[self.name] = self.form(self.req.POST)

    def _valid(self):
        return self.ctx[self.name].is_valid()

    def executor(self, action=None):
        if self.req.method == 'POST':
            self._binding()
            if self._valid():
                return action()

    def save(self):
        self.ctx[self.name].save(self.req.user)
        return True

    def create(self):
        self.ctx[self.name].create_user()
        return True

    def user_login(self):
        login(self.req, self.ctx[self.name].user)
        return True
