import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自Miracle的测试邮件', 'xztjut@163.com', 'zx1994@vip.qq.com'
    text_content = '欢迎访问Miracle主页'
    html_content = '<p>欢迎访问<a href="https://weibo.com/Miraclezx?refer_flag=1005055010_" target=blank>www.sinablog.com</a>，这里是张旭的微博主页！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()