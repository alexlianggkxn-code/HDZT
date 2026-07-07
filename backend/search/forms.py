import random
import string

from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.core.exceptions import ValidationError


def make_captcha_code() -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(4))


class CaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    captcha = forms.CharField(
        label="验证码",
        max_length=4,
        widget=forms.TextInput(attrs={"autocomplete": "off", "placeholder": "请输入右侧验证码"}),
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.request = request
        if request is not None and request.method != "POST":
            request.session["admin_login_captcha"] = make_captcha_code()
        if request is not None and not request.session.get("admin_login_captcha"):
            request.session["admin_login_captcha"] = make_captcha_code()

    def clean_captcha(self):
        value = (self.cleaned_data.get("captcha") or "").strip().upper()
        expected = ""
        if self.request is not None:
            expected = self.request.session.get("admin_login_captcha", "")
        if not expected or value != expected:
            if self.request is not None:
                self.request.session["admin_login_captcha"] = make_captcha_code()
            raise ValidationError("验证码不正确，请重新输入。")
        return value
