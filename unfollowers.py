# imports
from instapy import InstaPy
from instapy import smart_run
import os
from time import sleep

# login credentials
bot_username = input("Bot username: ")
bot_password = input("Bot password: ")

username = input("Desired username to check for unfollowers: ")

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=bot_username,
                  password=bot_password,
                  headless_browser=False)

with smart_run(session):
  # get old followers
  filename = username + '_followers.txt'
  old_followers = []
  if not os.path.isfile(filename):
    old_followers = session.grab_followers(username=username, amount="full", live_match=True, store_locally=False)
    with open(filename, 'w') as f:
      for follower in old_followers:
        f.write(follower)
        f.write('\n')
  else:
    with open(filename) as f_obj:
      for line in f_obj:
        old_followers.append(line.rstrip())

  # get new followers
  new_followers = session.grab_followers(username=username, amount="full", live_match=True, store_locally=False)

  # compare old and new followers
  unfollowers = []
  for old_follower in old_followers:
    if old_follower not in new_followers:
      unfollowers.append(old_follower)

  # show unfollowers
  print(unfollowers)

  # update followers.txt
  os.remove(filename)
  with open(filename, 'w') as f:
      for follower in new_followers:
        f.write(follower)
        f.write('\n')
