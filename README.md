# InstaFollower bot


## Introduction



This is a script written in python to automate following on instagram users with similar interests.
Very recommended for starter business to grow their follower crowd


## Prerequisites

Before you can use InstaFollower Bot, you'll need to have the following installed:
- Python 3.10
- Selenium

## Setup


1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory using `cd`.
3. Install the required dependencies by running pip install -r requirements.txt.
4. Add Your username, password and the similar account in the main.py file.
      
       Line 107: USERNAME = 'Your username'
       Line 108: PASSWORD = 'Your password'
       Line 109: SIMILAR_ACCOUNT = 'Similar to your page'

5. Run the script using `python main.py`.
6. The script will log in to your Instagram account, navigate to the Instagram page 
of the specified user, and follow their followers automatically.
7. In case instagram suspects the bot, it will the 5 minutes break and continue following

## Contributing

If you want to contribute to InstaFollower Bot, feel free to submit a pull request. 
Please make sure to follow the existing code style and include tests for any new features.