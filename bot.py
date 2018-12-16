#Written by Tyler Paplham
import praw
import botinfo
import mysql.connector

cursor = botinfo.mydb.cursor()
reddit = praw.Reddit(botinfo.BOT, user_agent= botinfo.BOT_AGENT)
key_phrases = ['kill myself', 'want to die', 'suicidal thoughts']
subreddits_monitor = ['depression', 'depression_help']
response_txt = "Hey, I noticed your post mentions suicidal thoughts and I wanted let you know you are not alone. If you would like to talk to someone you can reach out to the National Suicide Prevention Lifeline at 1-800-273-8255 (or you can chat online [here](https://suicidepreventionlifeline.org/chat/)). They are a great resource to go to even for just venting about stressors.\n\nIf you are located outside of the USA you can go [here](http://ibpf.org/resource/list-international-suicide-hotlines) to find a local lifeline number to reach out to.\n\n -------------------------\nThis is a bot. If you would like to report a bug or issue please message this account directly."

def contains_phrase(submission):
    normalized_title = submission.title.lower()
    normalized_self = submission.selftext.lower()
    if any(P in normalized_title for P in key_phrases) or any(P in normalized_self for P in key_phrases):
        return True
    else:
        return False

def responded(submission):
    current_id = submission.id
    query = "SELECT id FROM posts WHERE id = '" + current_id + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    if result == []:
        return False
    else:
        return True

def respond(submission):
    submission.reply(response_txt)
    log_response(submission.id)

def log_response(id):
    query = "INSERT INTO posts (id) VALUES ('" + id + "')"
    cursor.execute(query)
    botinfo.mydb.commit()

def subs(subreddits_monitor):
    length = len(subreddits_monitor)
    count = 1
    s = ""
    for sub in subreddits_monitor:
        if count < length:
            s += sub + "+"
            count += 1
        else:
            s += sub
    return s

if __name__ == "__main__":
    #fetch submission in a subreddit on depression and repeat indefenitely
    sublst = subs(subreddits_monitor)
    for submission in reddit.subreddit(sublst).stream.submissions():
        if contains_phrase(submission):
            print("Found: " + submission.title + " --> " + submission.id)
            if not responded(submission):
                respond(submission)
                print("[REPLY COMPLETED]")
            else:
                print("[ALREADY RESPONDED]")
    print("Program Terminated. Loop Ended.")