# Note: You can use slicing, split and partition to achieve the same result.
# Only the implementation differs in each case

# Using Split
email_id = input("Please enter your email ID: ")
username_domain = email_id.split('@')
username = username_domain[0]
domain = username_domain[1]
print("Username:", username)
print("Domain:", domain)

#Using slicing
atrate = email_id.find('@')
username = email_id[:atrate]
domain = email_id[atrate+1:]
print("Username:", username)
print("Domain:", domain)
