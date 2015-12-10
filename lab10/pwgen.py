from passlib.hash import md5_crypt

class Generate(object):
	
	def run(self):
		
		# Read in the users file of usernames and passwords
		userList = {}
		f = open('userListw.txt')
		for user in f:
			UserPassword = user.split()
			userList[UserPassword[0]] = UserPassword[1]

		f.close()
		print userList
		
		# Generate the password hasheds for the shadow file
		salt = 'salt'
		hashedPasswords = {}
		for user in userList:
			h = md5_crypt.encrypt(userList[user])
			hashedPasswords[user] = h
			print '{} - {}'.format(user,userList[user])
			print '{}:{}'.format(salt, h)
		
		# Generate the passwd file
		homeDir = '/home/eclazalde'
		shell = '/bin/bash'
		userInfo = 'Generated user'
		uid = 1001
		pwFile = open('passwd', 'w')
		for user in userList:
			line = ('{}:{}:{}:{}:{}:{}:{}\n').format(user, 'x', uid, uid, userInfo, homeDir, shell)
			pwFile.write(line)
			uid += 1
		
		# Generate the shadow file
		endString = '14538:0:99999:7:::'
		shFile = open('shadow', 'w')
		for user in hashedPasswords:
			line = ('{}:{}:{}\n').format(user, hashedPasswords[user], endString)	
			shFile.write(line)	

if __name__ == '__main__':
    Generate().run()
