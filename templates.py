
post_reviewer_prompt = """

rewrite the following linkedin [POST] following these rules:
1. use a very simple english that even non natives can understand easily
3. if a concept is not clear and requires a bit of expanding, do it.
2. Dont use the following phrases and words:
revolutionize
dive in
venture 
innovative
realm
Adhere
Delve
Reimagine
Robust
Orchestrate
Diverse
Commendable
Embrace
Paramount
Beacon
Captivate
Commendable
Advancement in the realm
Aims to bridge
Aims to democratize
Aims to foster innovation and collaboration
Becomes increasingly evident
Behind the Veil
Breaking barriers
Breakthrough has the potential to revolutionize the way
Bringing us
Bringing us closer to a future
By combining the capabilities
By harnessing the power
Capturing the attention
Continue to advance
Continue to make significant strides
Continue to push the boundaries
Continues to progress rapidly
Crucial to be mindful
Crucially
Cutting-edge
Drive the next big
Encompasses a wide range of real-life scenarios
Enhancement further enhances
Ensures that even
Essential to understand the nuances
Excitement
Exciting opportunities
Exciting possibilities
Exciting times lie ahead as we unlock the potential of
Excitingly
Expanded its capabilities
Expect to witness transformative breakthroughs
Expect to witness transformative breakthroughs in their capabilities
Exploration of various potential answers
Explore the fascinating world
Exploring new frontiers
Exploring this avenue
Foster the development
Future might see us placing
Groundbreaking way
Groundbreaking advancement
Groundbreaking study
Groundbreaking technology
Have come a long way in recent years
Hold promise
Implications are profound
Improved efficiency in countless ways
In conclusion
In the fast-paced world
Innovative service
Intrinsic differences
It discovered an intriguing approach
It remains to be seen
It serves as a stepping stone towards the realization
Latest breakthrough signifies
Latest offering
Let’s delve into the exciting details
Main message to take away
Make informed decisions
Mark a significant step forward
Mind-boggling figure
More robust evaluation
For instance
Navigate the landscape
Notably
One step closer
One thing is clear
Only time will tell
Opens up exciting possibilities
Paving the way for enhanced performance
Possibilities are endless
Potentially revolutionizing the way
Push the boundaries
Raise fairness concerns
Raise intriguing questions
Rapid pace of development
Rapidly developing
Redefine the future
Remarkable abilities
Remarkable breakthrough
Remarkable proficiency
Remarkable success
Remarkable tool
Remarkably
Elevate 
Captivate 
Tapestry 
Delve 
Leverage 
Resonate 
Foster 
Endeavor 
Embark 
Unleash 
Renowned
Represent a major milestone
Represents a significant milestone in the field
Revolutionize the way
Revolutionizing the way
Risks of drawing unsupported conclusions
Seeking trustworthiness
Significant step forward
Significant strides
The necessity of clear understanding
There is still room for improvement
Transformative power
Truly exciting
Uncover hidden trends
Understanding of the capabilities
Unleashing the potential
Unlocking the power
Unraveling
We can improve understanding and decision-making
Welcome your thoughts
What sets this apart
What’s more
With the introduction
Bespoke
Whimsical
Meticulous
Emerge
Refrain
Vibrant
Reimagine
Evolve
Supercharge
Pivotal

---
[Post]= 
{post}



"""

prompt_short_to_post = """

You are an expert in crafting Linkedin Posts.

I will provide you with a [short_video_transcript] and set of successfull post [Templates]

Your task is to anlyze the [short_video_transcript] and turned into a linkedin post.

Choose the best template from the list, and use it to craft my next viral post.

Rules to follow:
Do not include hashtags or external links.
Call-to-Action (CTA): Include questions or prompts that encourage comments and shares.
Target Audience: People intersted in AI and business and self improvement.


[Templates]:

{post_templates}


-----------------------

[short_video_transcript]:

{video}


---------------

"""

prompt_1 = """

You are an expert in crafting Linkedin Posts.

I will provide you with a [Blog_Post] and set of success post [Templates]

and your task is to anlyze my [Blog_Post] and extract the idea that can be turned into a linkedin post.

Then choose the best template from the list, and use it to craft my next viral post.

Rules to follow:
The Post should not include vivid steps or info, like "prepare your system" "click here", it should be clear and contains all necessary information.
Do not include hashtags or external links.
Call-to-Action (CTA): Include questions or prompts that encourage comments and shares.
Target Audience: People intersted in AI and Automation in Marketing and business.


[Templates]:

{post_templates}


-----------------------

[Blog_Post]:

{blog}


---------------

"""

templates_1 = """

Template #1: "How to / The Secret to" Template

Description:

This template is designed to create LinkedIn posts that offer a step-by-step guide or reveal the secret to achieving a specific goal or solving a problem. The post begins with an attention-grabbing headline like "How to {Do This Thing}" or "The Secret to {Getting Desired Outcome}". It then lists several steps or traits (usually 3-5), each with a short description. The post concludes with a call-to-action (CTA) that encourages readers to access a free guide or resource linked in the comments.

Example:

How to create a killer Intro Section on your LinkedIn profile (5 little-known steps anyone can use)

Background photo: Use a 'soft' CTA.
Name: No confusing letters or jargon words.
Profile pic: Smile, look at the camera, no distractions.
Headline: Niche, problem, outcome of solving problem.
Empathy: Deeply understand your audience through research.
If you want to make your LinkedIn profile 10x better, there's a free guide in the chit chat below.

Template #2: "The Rant" Template

Description:

Use this template to create posts that express frustration or dissatisfaction about a particular issue relevant to your audience. Start by hinting that a rant is coming to grab attention. Pose a question about why the negative thing happens, and share your personal experience with it. Exaggerate the effects to emphasize the impact and list steps you're taking to address the problem. Conclude by inviting your audience to share how they handle similar situations, stimulating discussion.

Example:

I'm sorry but I'm going to have a little rant today...

Why do people book calls and then not show up?

I've had 5 no-shows this week and I'm feeling very frustrated by it!

I get that people can sometimes miss reminders or something unexpected comes up, but those things should be exceptions.

I don't even mind so much when people genuinely forget (we're all human) but at least they're apologetic about it.

Most of the people that didn't show up didn't even acknowledge it, even after I sent a very pleasant email and direct message. That's just rude!

I'm tired of people not respecting my time so I've decided to do 4 things:

Make it way harder for people to book calls with me by 'tightening up' my application form and kicking out the tire-kickers.
Tag people who don't show up in my CRM so they have to jump through hoops to book again.
Ensure the SMS reminder option is available for all bookings.
Send a direct message to confirm they will actually make it!
Hopefully, that will cut down the no-shows!

OK, rant over—thanks for letting me vent! 😅

I'm curious, how do you handle no-shows? And what do you do to minimize them?

Template #3: "Polarization" Template

Description:

This template is for creating posts that present a controversial or polarizing statement to spark debate and engagement. Start with a bold statement that challenges common beliefs. Provide reasoning and evidence to support your viewpoint. The goal is to split your audience and encourage them to engage by agreeing or disagreeing. End with a call-to-action inviting them to share their thoughts.

Example:

Becoming a coach is easy.

Creating a business around it is not.

Why do most coaches scrape by while only a few thrive and prosper?

I've spoken to thousands and worked with hundreds of coaches over the last few years, and there are some commonalities I see that differentiate successful coaches from the rest:

Unshakable belief: They believe deeply in their ability to get incredible results for clients.
Clear niche: They are crystal clear about whom they work with and understand their niche's problems.
Consistency: They plan and execute daily activities needed to run their business.
Entrepreneurial spirit: They know it's not enough to be an awesome coach; they need to be awesome entrepreneurs.
Seek help: They get guidance from those who've succeeded before them.
If you're a coach and want to be successful, adopting these traits could make a significant difference. Are you up for that?

I'd love to know if you agree or disagree. Tell me in the comments, please. 😁

Template #4: "Data-Driven" Template

Description:

Create posts that leverage impactful statistics to highlight a problem or opportunity in your industry. Start with a compelling statistic that contrasts with another fact to create intrigue. Outline the main reasons for this discrepancy, providing supporting information for each. Conclude with a CTA directing readers to a resource linked in the comments.

Example:

The life coaching industry is estimated to be worth $2,400,000,000. Yet 56% of coaches are earning less than $1,000 per month.

There are three main reasons for this:

Lack of niche: Without focusing on a specific group, marketing messages fail to break through the noise.
Inability to create leads: Not knowing how to guide conversations can result in missed opportunities.
Shallow audience understanding: Without deep insights into their audience's problems and desires, coaches struggle to connect.
If you want to avoid being in the bottom 95%, check out my digital course below.

COMMENTS

https://in.linked.coach/li-po-lbf-as-

Template #5A: "Three Things" Template

Description:

Use this template to present three actionable tips or steps to achieve a desired outcome. Start by stating that there are three things that will help achieve an awesome result and pique interest by asking if the reader wants to know what they are. List each point with a brief explanation. Conclude with a CTA to access more detailed information in the comments.

Example:

There are 3 things you can do right now on LinkedIn to help grow your network.

Wanna know what they are?

Here you go...

Optimize your profile picture: A good profile picture makes it 7 times more likely that someone will connect with you.
Create a profile video: Seeing and hearing you builds a stronger human connection.
Create a voice note: Use the name pronunciation feature to include a short call to action.
If you want to know exactly how to do these 3 things, there's a guide in the chit chat below. 👇

Happy Saturday 😁

COMMENTS: Here's a lesson from my online course—The LinkedIn Business Formula. Hope it's helpful!

https://linked.coach/lc-li-business-formula-teaser

Template #5B: "Three Things Every [Topic] Should Include" Template

Description:

This template lists three essential elements that every [topic] should have, each with a short explanation. Emphasize the importance of these elements and provide tips on how to get them right. Conclude with a CTA to read a free guide in the comments to avoid common mistakes.

Example:

3 Things Every Good LinkedIn Headline Should Include:

The people you help: The narrower the niche, the better.
The problem you help them solve: Ask them about their problems.
The outcome they get by solving the problem: Ask them what they want.
The only real way to get this right is to:

Be crystal clear on who your niche is.
Reach out to them for research.
Write down what they tell you exactly as they say it.
To avoid making the mistakes most people make with their headline, read the free guide on how to set up your LinkedIn Intro Section in the chat below.

Template #5C: "Activity is Simple—If You Know How" Template

Description:

Assert that a particular activity is simple if you know how, highlighting that it involves doing three things well. List the three critical tasks and invite the reader to assess how well they're doing them by taking an action (e.g., a quiz or health check) provided in the comments. Encourage engagement by asking readers to share their results.

Example:

Generating leads for a coaching or consulting business on LinkedIn is simple—if you know how.

You just have to do 3 things well.

Wanna know what they are and how well you're doing them?

Set up your profile to attract your ideal clients.
Create content consistently that delivers value to your audience.
Connect with the right people in a way that makes them want to pay for your services.
To find out how well you're doing them, go to the chit chat below to take the LinkedIn Health Check.

I'd love to know your score. Tell me below if you're feeling brave. 😉



"""

templates_2 = """


Template #1: Narrative Approach
Stories have always captivated us, and for good reason.

They connect with us on an emotional level, making messages both entertaining and memorable.

That's why incorporating stories into your LinkedIn posts can be incredibly effective for capturing attention, building rapport, and encouraging engagement.

You can share a wide variety of stories on LinkedIn, including:

personal anecdotes,
business milestones,
success stories,
case studies, or
customer testimonials.

Template Instructions for a Story-Driven LinkedIn Post
-Begin with a personal anecdote: Start your post with a memorable or significant personal story.

-Share your initial emotions: Describe how you felt during this experience to connect emotionally with your readers.

-Introduce the turning point: Highlight the moment that changed the course of the events you are describing.

-Describe the outcome: Explain what happened as a result of the turning point.

-Reflect on the experience: Share insights or lessons learned from the experience.

-Offer encouragement and a takeaway: Provide a motivational insight or actionable advice that readers can apply in their own lives.

-Engage your readers with a question: Conclude with a question tha


Example:
"I remember the first time I spoke in front of 200 people.

I was incredibly nervous, and my ears turned red, which only made me more anxious.

Despite my fears, they called my name, and I stepped onto the stage.

Fifteen minutes later, I had finished my presentation.

It wasn't perfect, but it was a huge personal success.

This experience made me reconsider the opportunities I had missed by staying in my comfort zone.

Now, whenever I doubt my presentation skills, I remind myself, ‘If you did it once, you can do it again.’

How about you? Are you comfortable stepping out of your comfort zone? How did you learn to embrace it?"


---

Template #2: Observational Insights
Observations are a daily part of human nature.

We observe people, events, and the world at large, which helps us form opinions, develop ideas, and learn.

Sharing these observations on LinkedIn is an excellent way to:

spark conversations,
provoke thought, and
engage your audience.
You can discuss anything from industry trends and current events to business insights and life lessons—anything that might interest or add value for your followers.


Template Instructions for an Observation-Based LinkedIn Post
- Start with what you observed: Initiate your post by describing a common discussion or trend you've noticed.

- Share your insight: Comment on the quality or accuracy of the observed trend or discussion.

- Reflect on why this might be: Analyze and explain possible reasons behind what you've observed.

- Conclude with a realization: Share a personal realization or broader conclusion you've drawn from your observation.

- Offer advice: Provide practical advice based on your conclusions that your audience can apply.

- Engage your audience with a question: Finish with a question that prompts your readers to reflect and respond, fostering engagement.

Example in Action
"I see many people on LinkedIn discussing the power of personal branding.

But I've noticed that much of the advice given is less than stellar.

It seems many offer suggestions that sound good, without real-world experience to back them up.

This made me realize that genuine expertise is rare, and it's crucial to verify someone's credentials before taking their advice.

Always research thoroughly and confirm the results someone claims, ensuring their guidance is reliable and applicable.

What's the best and worst advice you've ever received about LinkedIn? Share your experiences in the comments below!"


---

Template #3: Contrarian Perspective

Taking a contrarian stance on a popular issue, topic, or belief is a powerful way to differentiate yourself and drive engagement on LinkedIn—or any social media platform.

It’s not about being controversial for the sake of it, but rather presenting a well-reasoned, researched opinion that challenges mainstream ideas.

This approach can capture attention and spark meaningful discussions.



Template Instructions for a Contrarian Perspective LinkedIn Post
-State the common belief: Begin by stating a widely accepted opinion or belief.

-Introduce your contrasting viewpoint: Offer your differing perspective clearly and assertively.

-Explain your reasoning: Detail the reasons behind your viewpoint, providing logical explanations or evidence.

-Propose an alternative: Suggest a more beneficial or reasoned approach as an alternative to the common belief.

-Engage your audience: Encourage interaction by asking for their opinions on the topic.

-Call to action: Prompt your readers to engage further by commenting on the post.

Example in Action
"Many people believe that to be successful, you must hustle 24/7.

However, I think this is bad advice.

Constant hustling leaves no room to relax, recharge, or reflect, which are essential for peak performance and innovation.

Instead of maintaining a non-stop work ethic, incorporating regular downtime into your schedule is crucial.

What's your take on the 'hustle 24/7' mentality? Share your thoughts in the comments below!"


----

Template #4: Comparative Analysis
Comparisons are a fundamental way we make sense of the world.

By comparing people, experiences, products, and services, we gain a better understanding of their relative value and context.

This is why comparison-based content is so engaging and effective, especially on platforms like LinkedIn.

Using comparisons in your posts can vividly highlight differences, clarify your points, and present information in a new light, naturally boosting engagement.

Template Instructions for a Comparison LinkedIn Post
👉 Introduction: Briefly introduce the two items or concepts you are comparing.

👉Thing A:

Trait 1: Describe the first characteristic.
Trait 2: Describe the second characteristic.
Trait 3: Describe the third characteristic.
Trait 4: Describe the fourth characteristic.
👉Thing B:

Trait 1: Describe the first characteristic of the second item, contrasting it with Thing A.
Trait 2: Describe the second characteristic, highlighting differences.
Trait 3: Describe the third characteristic, focusing on contrast.
Trait 4: Describe the fourth characteristic, underscoring how it differs from Thing A.
👉Call to Action (CTA): Engage your audience by asking them a question related to the comparison to encourage interaction.

Example in Action
"Let's compare the qualities of an average LinkedIn post versus a great one:

Average LinkedIn Post:

Boring
Uninspired
Doesn’t provide value
Overly promotional
Great LinkedIn Post:

Engaging
Interesting
Informative
Valuable

---

Template #5: Structured Listices
Listicles are incredibly popular because they're concise, easy to digest, and typically packed with valuable insights.

This format is especially effective on LinkedIn, where readers are always on the lookout for new tips, tricks, and strategies to enhance their personal and professional lives.

Providing this information in a straightforward, list-based format can significantly boost your engagement.

When crafting a listicle, you can consider various types, such as:

top [insert number] lists,
how-to lists, or
resources lists, depending on what will be most beneficial for your audience.


Template for a Listicle-Based LinkedIn Post
👉 Title: [X] Ways To [Achieve a Goal/Perform a Task]

👉 Introduction: Offer a compelling intro that sets the stage for your list.

👉 List Item 1: Title of Tip/Strategy

👉 Explanation: Provide a brief 1-2 sentence description or explanation.

👉 List Item 2: Title of Tip/Strategy

👉 Explanation: Another brief description. Continue with more items as needed.

👉 Conclusion: Summarize the key points or offer additional advice to wrap up the list.

👉 Engagement Prompt: End with a question or call to action to encourage comments and interaction.

Example in Action
“5 Ways To Up Your LinkedIn Posting Game

If you're looking to enhance engagement on your LinkedIn posts, improving your strategy is key. Here’s how you can start:

1. Be more personal.

Share more about your personal experiences and behind-the-scenes moments. This approach helps humanize your profile and makes you more relatable.

2. Provide value.

Ensure every post offers something beneficial to your audience, whether it's educational, entertaining, or inspiring.

3. Maintain consistency.

Regular posting is crucial. Aim for a few times a week to maintain visibility and engagement.

4. Craft compelling hooks.

The first few lines of your post must grab attention and make people want to read more. Invest time in writing engaging hooks.

4. Format posts for readability.

Avoid large blocks of text by using paragraphs, subheadings, and white space to make your content easier to read.

Implement these strategies, and watch your LinkedIn engagement grow!



"""

templates_3 = """


Template #1 - Grab them, shake them, show them the light

This template requires a little reverse engineering and taking a different point of view of a situation all your followers can connect with. 

Example:
Traditional leadership is failing. Quiet quitting is on the rise.  And that’s a good thing. Let me tell you why.
Let’s analyse the example. 

Grab your followers’ attention with a situation/challenge/problem that they are working to overcome or they can all relate to. 
Introduce the result with the highest impact arising from this situation and flip it on its head. 
Look at the consequence from a different standpoint and write what you see. Be insightful, mention statistics and include your solution organically.
Traditional leadership is failing. Quiet quitting is on the rise. And that’s a good thing. Let me tell you why. The C-suite is finally understanding that the needs of employees have changed. That they need to invest in upskilling the company’s managers. That they need to transform and update operations. That they need to change the decision-making process. Or get out-competed. And die.


---
Template #2 - The downside you didn’t know about

Make a list of all the ways a popular tool, platform or tactic fails to accomplish user’s goals, then offer your solution.

Examples:
Here are 20 ways Google Analytics fails to track campaign success.
Here are 10 reasons you should stop spending money on outbound marketing.

---
Template #3 - I was shocked when he/she revealed the secret

Refer to a person of authority (subject matter expert, market leader, highly experienced professional) and list their most valuable insights.

Examples:
An investor with 30 years of experience told me the ingredients of a successful business. I was surprised when he revealed these secrets. Here is what he told me: 
An HR director working for a billion-dollar business told me what I should do to build a successful company culture. I was amazed when she revealed this little-known strategy. Here is what she told me.


---
Template #4 - Follow the process

This template is about teaching your connections how to complete a task or achieve an objective by applying a simple process. 
Use adjectives to describe the process and grab attention: easy, simple, essential, effortless, unique, little-known, verified, endorsed, step-by-step, no-hassle, successful etc. 
Mention what they achieve in the first sentence.

Examples:
Create the best Facebook campaign today. Here’s a verified 5-step process.
Write viral LinkedIn posts. Here's a simple 3-step process.

---
Template #5:  The ‘I can’t live without’ list.

Examples:
20 Chrome extensions I can’t live without.
5 daily apps I can’t do my job without. 
6 positive affirmations I can’t start my day without.
10 sales habits I couldn’t be successful without. 



"""

templates_4 = """

Template #1: "[X] Beginner Mistakes" Template

Description:

This template lists common beginner mistakes associated with a specific role or activity. It begins by stating the number of mistakes (X) and the role in question. Each mistake is listed succinctly. Optionally, you can add a bonus mistake at the end for emphasis. This template helps in educating the audience about pitfalls to avoid and can stimulate engagement.

Structure:

[X] beginner mistakes as a [role]:

[Mistake 1]

[Mistake 2]

[Mistake 3]

...

[Mistake X]

Most importantly... [Bonus Mistake]!
Example:

9 beginner mistakes as a content creator on X:

- Not engaging with others
- Using hashtags
- Not optimizing your bio
- Buying followers
- No personality in tweets
- Generic content
- Ignoring analytics
- Not utilizing threads
- Switching niches too often

And most importantly... expecting overnight success!

---

Template #2: "[Them] vs. [Us]" Template

Description:

This template contrasts two groups by listing negative actions associated with "Them" and positive actions associated with "Us." It's designed to create a polarizing effect that engages readers and encourages them to align with the positive behaviors. This format is effective for emphasizing differences in mindset, approach, or behavior between two distinct groups.

Structure:

[Them]:

[Bad Action 1]

[Bad Action 2]

[Bad Action 3]

[Bad Action 4]

[Bad Action 5]

[Us]:

[Good Action 1]

[Good Action 2]

[Good Action 3]

[Good Action 4]

[Good Action 5]
Example:

Short-term thinkers:

- React
- Rant
- Whine
- Blame
- Excuse

Long-term builders:

- Reflect
- Learn
- Improve
- Adapt
- Execute

---

Template #3: "[X] Ways to [Y]" Template

Description:

This template provides a list of methods or strategies to achieve a particular goal. It starts with a headline stating the number of ways (X) to accomplish something (Y). Each way is listed clearly and concisely. You can include a concluding statement to wrap up the list or encourage action. This format is ideal for sharing tips, advice, or actionable insights.

Structure:
[X] ways to [Y]:

[Way 1]

[Way 2]

[Way 3]

...

[Way X]

[Conclusion]
Example:

6 ways to get an endless stream of content ideas for Twitter:

- Use AI
- Ask your audience
- Check out competitors
- Look at trending topics
- Browse other platforms
- Bookmark interesting ideas


---
Template #4: "[Job] 101" Template

Description:

This template outlines basic principles or foundational advice for a specific job or role. It uses a "Don't [Negative Action], [Positive Action]" format to highlight common mistakes and their better alternatives. This structure helps in delivering clear do's and don'ts, making it easier for the audience to grasp essential concepts. A concluding statement can reinforce the main message or inspire the reader.

Structure:

[Job] 101:

Don't [Negative Action 1], [Positive Action 1]

Don't [Negative Action 2], [Positive Action 2]

Don't [Negative Action 3], [Positive Action 3]

Don't [Negative Action 4], [Positive Action 4]

Don't [Negative Action 5], [Positive Action 5]

[Conclusion]
Example:

Entrepreneurship 101:

- Don't borrow money, lend it
- Don't take a job, create one
- Don't dig for gold, sell shovels
- Don't see a problem, see a solution
- Don't buy them fish, teach them to fish

Freedom starts with becoming your own boss!


"""

CTAs = """

Strong CTA
Your CTA is what turns interest into action and readers into loyal followers.

Almost every LinkedIn post should include a strong CTA.

In other words, you want to make it super clear what you want your reader to do.

Here are a few examples of CTAs that I’ve found to work on LinkedIn:

“Follow for more”
“Comment [keyword] if you want me to send you my [downloadable]”
“Click here to learn more about [topic]”
Ask your audience a question about their opinion on a topic
“Buy now” (use sparingly so you don’t come across as being ingenuine)
My most effective CTAs encourage people to comment. This creates an engagement loop (the more comments you get, the larger your reach).

"""