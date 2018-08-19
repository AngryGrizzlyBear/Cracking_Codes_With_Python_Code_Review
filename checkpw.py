print('Enter your password.')
typedPassword = input()
if typedPassword == 'swordfish':
    print('Access Granted')
elif typedPassword == 'mary':
    print('Hint: The Password is a fish.')
elif typedPassword == '12345':
    print('That is really an obvious password.')
else:
    print('Access Deniedtu')
print('Done.')