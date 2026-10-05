# Full Name: Adham Muayad Hashem
class Admin:
    def __init__(self):  # الكونستركتر: ينشئ بيانات دخول المدير
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):  # فحص اسم المستخدم وكلمة المرور للمدير
        if username == self.username and password == self.password:  # إذا كانت بيانات الدخول صحيحة
            return True
        else:
            print("Wrong admin username or password.")
            return False