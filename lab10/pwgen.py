
class Generate(object):
	
	def run(self):
		
		# Read in the users file of usernames and passwords
		userList = {}
		f = open('userList.txt')
		for user in f:
			UserPassword = user.split()
			userList[UserPassword[0]] = UserPassword[1]

		f.close()
		print userList
		
		# Generate the password hasheds for the shadow file
		hashedPasswords = {}
		
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
		

if __name__ == '__main__':
    Generate().run()
