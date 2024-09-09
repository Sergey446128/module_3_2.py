def send_email(message, recipient, *, sender= 'University.help@gmail.com'):
    a = '@'
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if a not in recipient and sender:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        if sender == recipient:
            print('Нельзя отправить письмо себе!')
            break
        elif sender == 'University.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            break
        elif sender != 'University.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            break

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!','urban.fan@mail.ru', sender= 'urban.info@gmail.com')
send_email('Пожалуста исправте задание','urban.student@mail.ru', sender= 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru',sender= 'urban.teacher@mail.ru')
