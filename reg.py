#1
emails = ["zuck26@facebook.com", "page33@google.com", "jeff42@amazon.com"]

def email_splitter(email):
	username = email.split('@')[0]
	domain = email.split('@')[1]
	domain_name = domain.split('.')[0]
	domain_type = domain.split('.')[1]

	print('Username : ', username)
	print('Domain   : ', domain_name)
	print('Type 	: ', domain_type)
	print(“\n”)

for email in emails:
email_splitter(email) 

#2
import re
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""

List = re.findall(r'\b[bB]\w+', text)

result = []
for l in List:
    if l not in result:
        result.append(l)
        
print result
#3
to_be_removed = ".,;_" # all characters to be removed

s = """A, very   very; irregular_sentence"""
for c in to_be_removed:
    s = s.replace(c, ' ')

s.split()
