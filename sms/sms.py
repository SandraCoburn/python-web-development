# We can use twilio api to be able to send a text to a valid phone number with twilio
# Will have to install the twillio package here
# We will have to open an account in twilio website. They will give us a new number from we can text
# They will also give us an auth_token needed for this to work
# Then you can copy and paste the python code

from twilio.rest import Client

account_sid = '<acount number from twilio>'
auth_token = '<authorization token from twilio>'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="<number given by twilio",
    body='This sends a text to a number',
    to='<number text will be sent to>'
)

print(message.sid)