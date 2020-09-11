# imports
from instapy import InstaPy
from instapy import smart_run
from time import sleep

# login credentials
bot_username = input("Bot username: ")
bot_password = input("Bot password: ")

username = input("Desired username to check for unfollowers: ")

while True:
  # get an InstaPy session!
  # set headless_browser=True to run InstaPy in the background
  session = InstaPy(username=bot_username,
                    password=bot_password,
                    headless_browser=False)

  with smart_run(session):
    followers = session.grab_followers(username=username, amount="full", live_match=True, store_locally=False)
    print(followers)

  sleep(30)
