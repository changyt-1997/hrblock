import time
import imaplib
import email
from email.header import decode_header
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


def hotmail(email_address, password):

    # 连接到IMAP服务器
    imap_server = "imap-mail.outlook.com"  # IMAP服务器地址，请替换成你的邮箱提供商的IMAP服务器地址
    imap_port = 993  # IMAP服务器端口号，请根据邮箱提供商的要求修改

    # 连接到IMAP服务器
    imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)

    # 登录邮箱账户
    imap_connection.login(email_address, password)

    # 选择邮箱文件夹
    mailbox = "INBOX"  # 你可以选择其他文件夹，比如"Sent"表示已发送邮件文件夹
    imap_connection.select(mailbox)

    # 搜索并获取最新的10封邮件
    search_criteria = 'ALL'
    status, messages = imap_connection.search(None, search_criteria)
    message_ids = messages[0].split()
    body = ""
    # 获取邮件内容
    status, msg_data = imap_connection.fetch(message_ids[-1], "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            # 获取邮件正文
            if msg.is_multipart():
                for part in msg.walk():
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                        body = part.get_payload(decode=True)
                        if not body:
                            continue
                        body = body.decode()
            else:
                body = msg.get_payload(decode=True).decode()
    # 关闭连接
    imap_connection.logout()
    return body


def get_mail_hr(username, password, depth=0):
    mail_content = hotmail(username, password)
    # 使用正则表达式匹配验证码
    code_pattern = re.compile(r'<span[^>]*>(\d{6})</span></strong>')
    match = code_pattern.search(mail_content)
    print("正在提取验证码...")
    # 提取验证码
    if match:

        code = match.group(1)
        print(f"获取结果为：{code}")
        return code
    else:
        if depth < 20:
            time.sleep(2)
            get_mail_hr(username, password, depth+1)
        print("未检查到验证码，且超出重试次数")
        return None


if __name__ == '__main__':
    # eyrampierisa@hotmail.com----oZDNmmiZ19
    # code = get_mail_ins("eyrampierisa@hotmail.com", "oZDNmmiZ19")
    # print(code)
    # print(f"--{code}--")
    # print(type(code))
    # eysiaspesib@hotmail.com----iXLYkIBr11
    # pecynaagpoonk@hotmail.com----yIEWBoeO68
    # crnicexlb@hotmail.com----uub4iD4625
    # bajaltrn7@hotmail.com----NE1zPOUg75
    get_mail_hr("rhynshivid@hotmail.com", "M29S2GlJ54")
