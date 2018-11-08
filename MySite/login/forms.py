# 我们前面都是手工在HTML文件中编写表单form元素，然后在views.py的视图函数中接收表单中的用户数据，
# 再编写验证代码进行验证，最后使用ORM进行数据库的增删改查。
# 这样费时费力，整个过程比较复杂，而且有可能写得不太恰当，数据验证也比较麻烦。
# 设想一下，如果我们的表单拥有几十上百个数据字段，有不同的数据特点，如果也使用手工的方式，
# 其效率和正确性都将无法得到保障。有鉴于此，Django在内部集成了一个表单功能，
# 以面向对象的方式，直接使用Python代码生成HTML表单代码，专门帮助我们快速处理表单相关的内容。
#
# Django的表单给我们提供了下面三个主要功能：
#
# 准备和重构数据用于页面渲染；
# 为数据创建HTML表单元素；
# 接收和处理用户从表单发送过来的数据。
# 编写Django的form表单，非常类似我们在模型系统里编写一个模型。
# 在模型中，一个字段代表数据表的一列，而form表单中的一个字段代表<form>中的一个<input>元素。

from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput
    (attrs={'class': 'form-control'}))
    # max_length限制字段输入的最大长度。它同时起到两个作用，
    # 一是在浏览器页面限制用户输入不可超过字符数，
    # 二是在后端服务器验证用户输入的长度也不可超过。

    # widget = forms.PasswordInput用于指定该字段在form表单里表现为
    # < input type = 'password' / >，也就是密码输入框。
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='确认密码', max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.CharField(label='邮箱地址', max_length=128, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
