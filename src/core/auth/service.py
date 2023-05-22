from .schema import Login


class AuthService():
    def login(self, dto: Login):
        return {'message': 'login success'}
           