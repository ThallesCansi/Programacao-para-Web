import re

username = input('User name (use only alphanumeric characters): ')
password = input('Password (use only alphanumeric characters): ')

newUsername = re.sub('[^A-Za-z0-9]+', ' ', username)
newPassword = re.sub('[^A-Za-z0-9]+', ' ', password)

print(f'Your username: {newUsername}')
print(f'Your password: {newPassword}')