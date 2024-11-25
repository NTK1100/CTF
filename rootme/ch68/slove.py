class MainActivity:
    def __init__(self):
        self.ed1 = None  # Giả sử đây là phần mà người dùng nhập vào
        self.seed = "2131689594"  # Giá trị chuỗi seed giả định từ file strings.xml
    
    def make_flag(self, s):
        a = s[5]
        _b = s[2]
        
        for s_ in range(len(s)):
            b = _b[-s_:] + _b[s_:]  # b = _b.substring(_b.length() - s_) + _b.substring(s_)
            
            if s_ >= 3:
                _b2 = _b + s[s_ - 3]  # _b2 = _b + s.charAt(s_ - 3)
            else:
                _b2 = _b + s[len(s) - (3 - s_)]  # _b2 = _b + s.charAt(s.length() - (3 - s_))
            
            if s_ >= len(_b2):
                _b = _b2 + s[s_ - len(_b2)]  # _b = _b2 + s.charAt(s_ - _b2.length())
            elif len(s) >= len(_b2) - s_:
                _b = _b2 + s[len(s) - (len(_b2) - s_)]  # _b = _b2 + s.charAt(s.length() - (_b2.length() - s_))
            else:
                _b = _b2 + s[len(s) - ((len(_b2) - s_) - len(s))]  # _b = _b2 + s.charAt(s.length() - ((_b2.length() - s_) - s.length()))
            
            a += b[((len(s) + len(_b)) * s_ + len(_b)) % len(b)]  # a = a + b.charAt((((s.length() + _b.length()) * s_) + _b.length()) % b.length())
        
        return a[:2] + s[3] + a[3] + '0' + a[5:7]

    def on_click(self):
        # Giả sử ed1 chứa dữ liệu từ người dùng nhập
        user_input = self.ed1  
        
        if user_input == self.make_flag(self.seed):
            print("Well played! You can validate now with this password :)")
        else:
            print("Try again ;)")

# Giả lập sự kiện khi người dùng nhấn nút
activity = MainActivity()
activity.ed1 = "8315042"  # Giả lập người dùng nhập vào đúng mật khẩu
activity.on_click()  # Chạy hàm onClick khi người dùng nhấn nút
