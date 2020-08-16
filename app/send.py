from twilio.rest import Client

account_sid = 'AC4cfd338ef202fe24bd7ea2a735a2337e'
auth_token = 'c153fe906e40c900fb9f3929348e914f'

client = Client(account_sid, auth_token)

def sendSMS(student,text):
  message = client.messages.create(
                                body=text,
                                from_='+12512201952',
                                to='+91'+student
                            )
  print(message.sid)

def sendWhatsapp(student,text):
  message = client.messages.create(
                                body='Hello there!',
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+91'+student
                            )

  print(message.sid)

sendSMS("7020402120", "hello world from twilio")
sendWhatsapp("7020402120", "hello world from twilio")
