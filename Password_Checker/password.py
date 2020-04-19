# Check if the password has ever been hacked

import requests, hashlib, sys

def request_api_data(query):                                                    # Returns all available tail hashes of 'query' hash
   url = 'https://api.pwnedpasswords.com/range/' + query
   res = requests.get(url)
   
   if res.status_code != 200:
      raise RuntimeError(f'Error {res.status_code}, please check api')

   return res

def password_hack_count(hashes, hash_to_check):                                  # compare the tail hashes
   hashes = (line.split(':') for line in hashes.text.splitlines())               # Split into tuple

   for h, count in hashes:
      if h == hash_to_check:
         return count
   return 0                                                                      # Tail hash isn't found

def pwned_api_check(password):
   sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()    # sha1 password hashing
   first_5, tail = sha1_password[:5], sha1_password[5:]
   response = request_api_data(first_5)

   return password_hack_count(response, tail)

def user_password(user_password):
   hack_count = pwned_api_check(user_password)
   if hack_count != 0:
      print(f'\nThe password: {user_password} has been hacked {hack_count} times.\n')
   
   else:
      print(f'\nThe password: {user_password} has not been hacked...yet\n')

   return (':)')

sys.exit(user_password(sys.argv[1]))

