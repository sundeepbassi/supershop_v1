2
Alan profile	
Alan
Away
8:34 pm in Dublin, Ireland
Alan profile
Alan
Away
Begin a Tutoring Session
Tutoring at Code Institute profile
Please confirm that you have prepared for this session as per the steps on this page: https://code-institute-org.github.io/tutoring-info/guidelines/ 
You should have:
A clear description of your issue
A list of the debugging steps and research you have carried so far 
Failure to answer all of the bots questions will result in this conversation being closed.
By clicking "I'm Prepared," you agree to these conditions.
I'm Prepared
Your tutoring usage time for this week (in minutes): 79
Tutoring at Code Institute profile
Please provide us with your Problem Statement. This is a clear description of the problem that you're currently facing.
At the very least, you need to tell us what should your code be doing, and what is it actually doing?
If you are getting an error, please send a screenshot.
If you are working on a particular file, which file is it, and which lines of code?
Hi tutors I am doing the video number two for the deployment stage and I have done the process as shown in the video for git push heroku main and an error has come up in the terminal
Tutoring at Code Institute profile
What steps have you taken so far to resolve the issue, or to address current gaps in your knowledge?
Vague answers like "searched on Slack and Google" are not sufficient here. What specific steps have you taken? What code and debugging steps have you tried? What resources have you used (e.g. provide links to StackOverflow questions you have read)?
checked online
Tutoring at Code Institute profile
One final thing. Please share your code with us. 
If you are working on Gitpod, please set your workspace to shared, and send us the link to it. If you are working on a course challenge, please send the name of the challenge.
https://sundeepbass-supershopv1-6tuyxyxoq9v.ws-eu67.gitpod.io/
Tutoring at Code Institute profile
Thank you. We will get back to you as soon as possible. You can see how busy tutoring currently is on this page: https://code-institute-org.github.io/tutoring-info/status/
Note that if you have failed to sufficiently answer any of the above questions, tutors will have to re-ask you for the information, which will use up part of your weekly tutoring time allowance.

Alan profile
Hi there, Alan here, how are you today?
HI Alan good to hear from, you I am good thanks how are you doing
I followed the steps as shown in the video and these errors came up in the video
in the termnal
Alan profile
Im good thanks for asking :) ok so this is a common issue and its down to python versions and heroku - we have a ready made response, give me a sec
thanks Alan
If you're seeing a backports.zoneinfo error when deploying to Heroku in the terminal.
﻿You'll need to set a supported version of Python for Heroku 20 as your default Python version.
﻿
﻿To do this we need to create a file called "runtime.txt" and add a supported Python version to it from this list:
https://devcenter.heroku.com/articles/python-support#supported-runtimes
﻿
﻿python 3.8.10 will be used in the example below, enter your chosen supported version inside the quotes
﻿
﻿In the terminal please type:
﻿
﻿1. touch runtime.txt && echo "python-3.10.7" > runtime.txt
2. git add . && git commit -m "Add runtime.txt for heroku deployment"
3. git push origin main
4. git push heroku main
﻿
You should now see the project building output in the terminal.
2:13 pm
these are the current supported versions

so try python-3.10.7
Alan profile
and if that doesnt work try 3.9.14
Hi Alan I will give it a go
Alan profile
Cool :)
Hi Alan I created the runtime.txt file and I was not sure how to add the python-3.10.7 into it
you can just copy it in directly
python-3.10.7
then save / commit /push
wothout the ""
Alan profile
without

like that
Alan profile
remove the quotes and push as normal to heroku


sorry I sent the wrong screen shot
I have added it to the runtime.txt and I need to do the terminal commands now
you need to remove the "" from it

Alan profile
then save and do the commands for commiting and pushing

is that correct now
Alan profile
yes looks right so you need to add , commit push
sorry Alan my brain is running slow was up early doing this
Alan profile
you are fine, maybe take a break after this one so - once you push it will get rid of the backports error
note you have 5 mins left of tutoring time for the week
sorry Alan now the gitpod is playing up

Alan profile
you typed into the runtime.txt file

thanks
still not able to make a commit
everytime I do a commit the cursor jumps to the front

Alan profile
you are typing in the text file again - make sure you are clicked into the terminal correctly
thanks Alan I opened up a new terminal and it is working now
Alan profile
Excellent stuff :) as i said you have reached the cap for the week
I did a git push also
do I just carry on with the tasks above
Alan profile
so continue on with the walkthrough and see how you get on, the cap is reset on monday
in the terminal
yep just carry on and you should be good
Alan profile
Best of luck with your project
Help Alan understand how they’re doing:
Tutoring at Code Institute profile
Rate your conversation
Terrible
Bad
OK
Great
Amazing
Bot · 1w ago.
Your conversation has ended

Send us a message


Hi tutors,
I followed the instructions that Alan sent me last week for deploying my project and I used
touch runtime.txt && echo "python-3.10.7" > runtime.txt
2. git add . && git commit -m "Add runtime.txt for heroku deployment"
3. git push origin main
4. git push heroku main
I also tried 3.9.14 and I got these errors in my terminal.
 
1:34 pm

What steps have you taken so far to resolve the issue, or to address current gaps in your knowledge?
Vague answers like "searched on Slack and Google" are not sufficient here. What specific steps have you taken? What code and debugging steps have you tried? What resources have you used (e.g. provide links to StackOverflow questions you have read)?


One final thing. Please share your code with us. 
If you are working on Gitpod, please set your workspace to shared, and send us the link to it. If you are working on a course challenge, please send the name of the challenge.
https://sundeepbass-supershopv1-6tuyxyxoq9v.ws-eu67.gitpod.io/

Thank you. We will get back to you as soon as possible. You can see how busy tutoring currently is on this page: https://code-institute-org.github.io/tutoring-info/status/
Note that if you have failed to sufficiently answer any of the above questions, tutors will have to re-ask you for the information, which will use up part of your weekly tutoring time allowance.





Hi Sunny, Ed here 👋
Just taking a look now 👍

Thanks Ed good to hear from you how are you doing buddy

Judging by that error message you ned to review your Procfile and ensure it's pointing to your app rather than boutique ado
ok ed I will have a look

This is the name of your project:

ok tyhanks E

is that ok and shall I follow Alans steps again

You shouldn't need to follow Alan's steps again. This is an H10 error pointing to your Procfile. If you update that and push changes then we hope the app will deploy this time 👍
0k I will do a git commit and push

I would remove the blank line in runtime.txt too
ok

If there's still issues with the deployment there are other things we can do to solve it
ok do i just git commit and push

Yes that's what I would try. There may be other issues but the Procfile is the main one for now 👍
I have done the push
git push heroku main do I use this command to deploy to heroku

OK, so you had committed those changes though? Can see changes to other files but presume you specified Procfile?

Your Heroku app should be connected to your Github repo? If so, just push to Github and wait for the automatic deployment to kick in for Heroku
I did just psuh with the procfie changes

sorry Ed how do i push to github
You must have, there are no pending commits 👍

Has you Heroku app deployed now?
I am not sure Ed

Can you load your Heroku app?
to be honest ed I do not know how to do it
been very stressful this weekend

OK, so the error you were getting was that your Heroku app was failing to deploy?
If so, go into Heroku and try to find your project.
yes when I was trying to deploy last week I tried with heroku from the terminal I will go ti the apps in heroku

I went inot heroku and tried to open the app and got this message


Let's fix the errors as I come across them:

Here you should not be splitting these strings across lines. So change to:
{
   'NAME': ('django.contrib.auth.password_validation.UserAttributeSimilarityValidator'),
   },
etc
ok ed I will give it a go


TIME_ZONE = 'UTC'
Not what you've got here:


OK so those changes were necessary, let me know what happens with next push
I changed it to 'UTC'


OK, let me know what happens with the Heroku build. We may have to remove those brackets from around this:

That was sloppy checking on my part, apologies.
No need to apologise Ed you have a heart of Gold mate

shall I git push again

I tried another push

Great, what does Heroku say now?
still the same as before


Can you please log into Heroku via your terminal?
heroku login -i

Logged in

Fab
heroku logs --tail
Let me know what it says



still mentioning gunicorn


It's saying you're trying to start with boutique_ado here.
Can you please send me a link to your GitHUB repo for this project? It sounds like Heroku isn't getting your changes
https://github.com/sundeepbassi/supershop_v1
https://github.com/sundeepbassi/supershop_v1

OK thanks, so the Procfile is correct there.
Please go into the Deployment tab on your Heroku app, and choose Manual Deploy from the bottom, pointing to the main branch
ok

sorry ed could not find manual deploy

Under Deployment method, choose Github and find your Github repo

do I just click enable automatic deploy
Yes that's fine too. But as we don't have a new deploy for it to see, on this occasion you'll need to go to the bottom and Manually deploy

After this, any time you push to Github it will automatically deploy to Heroku
sorry just seen manual deploy button

👍

do I click view now


Sounds like it deployed?
still getting the error

What does it say in the terminal now? Still referring to boutique ado?
Can you confirm that the build was successful according to the Heroku website?
I am not sure Ed the terminal still has errors


You need to add a SECRET_KEY variable to your Heroku cvars. Looks like we're making progress though, if the errors are changing :)

I feel we are getting there I think it has changed to supershop now
Yes!

Next thing is to fix that missing SECRET_KEY in Heroku cvars
How do I set the secret key

Settings in your Heroku app

I managed to do that

You will need to do this for all required environment variables.
At a minimum this will be:
SECRET_KEY
DATABASE_URL
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
Anything in your settings.py that comes from the environment
do I add all of them to the heroku config vars

is that ok

do I add those variables into the heroku now
or do i get them from the env.py file

they were added in the terminal

DATABASE_URL should already be there. You need to add SECRET_KEY (can be any value) and then get the others from Stripe
it wont let me copy and paste i will have to do it from the keyboard
I am trying to put data into the confid vars boxes and it will not let me

You need to edit each field and change its value. If in doubt delete the item and add it again
Thanks Ed I just worked it out I was rushing myself

Looks like your app is up and running now though? 🐶
ok I will give it a go still adding the variables

OK cool, I'd encourage you to get everything working locally before stressing too much about Heroku.
If you can get it working locally, you're in a good spot for the deployed app because your static files and everything are loading. That's a big hurdle :)
brilliant Ed

Just remember that Heroku 'config variables' are basically Heroku's version of 'env.py'
So any variables in settings.py which come from os.environ will need to be specified in your Heroku cvars
Thank you

OK, I'll close this chat now Sunny and wish you luck. It's great that your deployed app is working. Now you can focus on nailing the functionality and you should be golden 🌞
Thank you Ed you have been amazing guiding me through this
I did add my secret from the env.py file into heroku config vars is that ok
secret key
That's fine, it can be different between Gitpod and Heroku, just needs to be there 👍

Best of luck and do reach out again if you get stuck! 👋
Ed you are a life saver and I am very grateful for all your help and support have a great day buddy
😄

🌞
Help Ed understand how they’re doing:

You rated the conversation 
Thanks for letting us know
Ed truly has been amazing and is a brilliant tutor he has been very supportive in getting me to understand what is going on with the code and how best to fix the errors, Ed has restored my sanity and confidence and given me faith that I can do it. Ed is a great tutor.
Ed You are the best tutor and I appreciate all of your help you have a wonderful way of tutoring and because of my adhd it takes time for me to understand and absorb things and I am grateful that you have been very patient and kind.

Haha, you say that to all the tutors 😆
Glad you made some progress here, deployment is a stress at the best of times so you've done great 😄
Thank you yes but you are still the best don't tell them haha have a great day

Secret is safe with me 😉
🌟
Ed Thank you I have just deployed it to heroku

I think you already had?! 😆
😄

