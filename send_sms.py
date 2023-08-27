import os
from twilio.rest import Client


def verify(number):
    account_sid = 'ACf666ca9ca99cae6de36bc7c075821450'
    auth_token = 'bd80ccd9054a50fe91d195f017b1e92d'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="From VJTI | Your details were successfully added in our database!",
                        from_='+918689918042',
                        to='+91'+str(number)
                    )
    print('message sent !')
