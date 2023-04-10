# 记得要import
# 用于邮件解码
import pyzmail
# 用于登录
import imapclient


def get_mail(username, password):
    imapObj = imapclient.IMAPClient('outlook.office365.com', port=993)
    imapObj.login(username, password)
    select_info = imapObj.select_folder('Inbox', readonly=False)
    # 打印当前收件箱邮件数
    print('%d messages in INBOX' % select_info[b'EXISTS'])
    # 搜索未读邮件
    UIDS = imapObj.search('UNSEEN')
    # 如果未读邮件大于1 执行以下操作
    if len(UIDS) >= 1:
        for UID in UIDS:
            Rawmessages = imapObj.fetch(UID, [b'BODY[]'])
            messages = pyzmail.PyzMessage.factory(Rawmessages[UID][b'BODY[]'])
            # 获取邮件抬头
            emailtitle = messages.get_subject()
            # 打印邮件抬头
            print(emailtitle)
            # 获取邮件正文
            emailmessage = messages.text_part.get_payload().decode(messages.text_part.charset)
            # 打印邮件正文
            print(emailmessage)
            # 如果邮件内容包含 Test 则 返回HELLO
            if 'Test' in emailmessage:
                print('hello')
                return 'hello'
            # 否则的话就返回 error
            else:
                print('error')
                return 'erro'



# Send mail
# server.send_mail('yourfriend@example.com', {'subject': 'Hello!', 'content_text': 'By zmail.'})
# # Or to a list of friends.
# server.send_mail(['friend1@example.com', 'friend2@example.com'], {'subject': 'Hello!', 'content_text': 'By zmail.'})



if __name__ == '__main__':
    # puuhxwbmts@hotmail.com----Mc7FxjqR
    # get_mail("puuhxwbmts@hotmail.com", "Mc7FxjqR")
    import zmail

    server = zmail.server("puuhxwbmts@hotmail.com", "Mc7FxjqR")

    # Retrieve mail
    latest_mail = server.get_latest()
    zmail.show(latest_mail)