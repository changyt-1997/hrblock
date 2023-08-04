import time

import zmail, re


def get_mail(username, password, depth=0):

    server = zmail.server(username, password)

    # Retrieve mail
    latest_mail = server.get_latest()
    # print(latest_mail)
    mail_content = latest_mail['Content_html'][0]
    print(mail_content)
    # 使用正则表达式匹配验证码
    code_pattern = re.compile(r'<span[^>]*>(\d{6})</span>')
    match = code_pattern.search(mail_content)
    print("正在提取验证码...")
    # 提取验证码
    if match:
        print(f"获取结果为：{match}")
        code = match.group(1)
        return code
    else:
        if depth < 20:
            time.sleep(2)
            get_mail(username, password, depth+1)
        print("未检查到验证码，且超出重试次数")
        return None


def get_mail_ins(username, password, depth=0):

    server = zmail.server(username, password)

    # Retrieve mail
    latest_mail = server.get_latest()
    # print(latest_mail)
    mail_content = latest_mail['Content_html'][0]
    # print(mail_content)
    # 使用正则表达式匹配验证码
    code_pattern = re.compile(r'verification code is: (\d{6})')
    match = code_pattern.search(mail_content)
    print("正在提取验证码...")
    # 提取验证码
    if match:
        print(f"获取结果为：{match}")
        code = match.group(1)
        return code
    else:
        if depth < 20:
            time.sleep(2)
            get_mail(username, password, depth+1)
        print("未检查到验证码，且超出重试次数")
        return None


if __name__ == '__main__':
    # eyrampierisa@hotmail.com----oZDNmmiZ19
    code = get_mail_ins("eyrampierisa@hotmail.com", "oZDNmmiZ19")
    print(code)
    print(f"--{code}--")
    print(type(code))