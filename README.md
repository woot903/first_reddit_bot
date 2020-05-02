# Depression Watch Bot
### Background
I created this simple bot to learn the PRAW framework, which is used to interact with the popular forum site [reddit](wwww.reddit.com) through a bot account. The goal of this bot to identify people who are struggling with depression and suicidal thoughts and give them access to professional resources for help.

### Implementation
The bot identifies users on depression subreddits in need of help using a simple phrase list. The phrase list contains phrases that would typically come from an at risk user. The bot then replies to their post with a preset message containing links to professional hotlines for depression and managing suicidal thoughts.

This implementation uses PIP for package mangement.

### Areas for Future Development
* This bot uses a simple array of preset phrases to identify users. However, this list could be greatly expanded and stored more efficently using a JSON file to increase the bots ability to identify at risk users. Machine learning techniques like clustering could be used to help develop a more extensive list.

* The bot could utilize reddit's private messaging to feature to send links directly to users instead of responding to their posts.
