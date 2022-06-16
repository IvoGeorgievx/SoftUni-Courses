class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
lines = input()

while lines != "Stop":
    exploded = lines.split(" ")
    sender = exploded[0]
    receiver = exploded[1]
    content = exploded[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    lines = input()

send_email = list(map(lambda x: int(x), input().split(", ")))

for x in send_email:
    emails[x].sent()

for email in emails:
    print(email.get_info())
