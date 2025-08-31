from twilio.rest import Client

account_sid = 'AC5c86db3cc2ae75e844b48bcefc06d492'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+18323315443'
)

print(message.sid)