from twilio.rest import Client

account_sid = "AC0ce21a1c45f72517bfe03c41463479e0"
auth_token = "2d8e9a37da68fde46070a0b547c3c476"

client = Client(account_sid, auth_token)

message = client.messages.create(
	body = "Udacity on the first day of Eid and during World Cup? Are you a freak?",
	to = "+16504796958",
	from_ = "+12015001507")

print message.sid
