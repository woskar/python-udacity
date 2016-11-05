from twilio.rest import Client

account_sid = "{{AC039b3d75040ae2e9bb811e5cf009e00e}}" # Your Account SID from www.twilio.com/console
auth_token  = "{{e6f690d13d2e483cd01cd48f156c6ff3}}"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(to="+491752590108", 
    from_="+4917590108",
    body="Hello from Python! Here I am :D Hello World!")

print(message.sid)
