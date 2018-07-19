from sys import argv

script, user_name, age = argv
prompt = "-> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I know you are a %s years old people." % age
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
