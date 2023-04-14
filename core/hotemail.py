import time

import zmail, re


def get_mail(username, password, depth=0):

    server = zmail.server(username, password)

    # Retrieve mail
    latest_mail = server.get_latest()
    mail_content = latest_mail['Content_html'][0]
    # 使用正则表达式匹配验证码
    code_pattern = re.compile(r'\b\d{6}\b')
    match = code_pattern.search(mail_content)
    # 提取验证码
    if match:
        code = match.group(0)
        return code
    else:
        if depth < 10:
            time.sleep(2)
            get_mail(username, password, depth+1)
        print("未检查到验证码，且超出重试次数")
        return None


if __name__ == '__main__':
    # tpaapjj@hotmail.com----s69AP5BcGR
    code = get_mail("tpaapjj@hotmail.com", "s69AP5BcGR")
    print(code)