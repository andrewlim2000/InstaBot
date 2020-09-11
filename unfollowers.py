# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = input("Enter username: ")
insta_password = input("Enter password: ")

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  followers = session.grab_followers(username=insta_username, amount="full", live_match=True, store_locally=True)	
  all_unfollowers, active_unfollowers = session.pick_unfollowers(username=insta_username, compare_by="latest", compare_track="first", live_match=True, store_locally=True, print_out=True)
