# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
import datetime
from django.contrib.auth import get_user_model

from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

def add_one():
    '''
    Returns the next default value for the `ones` field, starts with 
    500
    '''
    if User.is_authenticated:
	    largest = Post.objects.filter(user=user).order_by('ones').last().ones
	    if not largest:
	        return 0
	    return largest + 1

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, related_name = 'postuser', null=True, blank=True, on_delete=models.CASCADE)
	question = models.CharField(max_length = 255)
	chapter = models.IntegerField()
	message = models.TextField(null=True, blank=True)
	create_date = models.DateField(default = datetime.date.today)
	publish_status = models.BooleanField(default=False)
	question_number = models.IntegerField(null=True)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse('tagr:post_detail',kwargs={'pk':self.pk, 'chapter':self.chapter})

	def publish_question(self):
		self.publish_question = True
		self.save()

	def next(self):
		try:
			return Post.objects.get(pk=self.pk+1)
		except:
			return None

	def previous(self):
		try:
			return Post.objects.get(pk=self.pk-1)
		except:
			return None


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
	if kwargs.get('created', False):
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=1, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=2, question='How does the story of Edwin C. Barnes inspire you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=3, question='When have you stopped "three feet from gold" in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=4, question='Can you think of examples when a "temporary defeat" turned into a victory in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=5, question='Are you willing to stake everything to move toward your burning desire?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=6, question='Would you categorize yourself as being "success conscious" or "failure conscious" up until now?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 1,question_number=7, question='What does the phrase "I am the Master of my Fate,  I am the Captain of my Soul" mean to you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=8, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=9, question='How does the story of the burning ships apply to you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=10, question='Have you found your "Statement of Desire"?  If not,  please do so and record it below?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=11, question='Does your "Statement of Desire" accurately reflect your burning desire?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=12, question='The turning point in the lives of those who succeed usually comes at the moment of some crisis,  through which they are introduced to their other selves.  What is the turning point in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=13, question='What does Napoleon Hill mean when he refers to the "their" ‘other selves’?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=14, question='What is the difference between "wishing for a thing" and "being ready to "receive it"?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 2,question_number=15, question='Are you truly ready to receive what you desire?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=16, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=17, question='How does Napoleon Hill define "faith"?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=18, question='How can you develop more Faith?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=19, question='What are affirmations?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=20, question='How can memorizing the "Self-Confidence Formula" positively affect your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 3,question_number=21, question='Both poverty and riches are the offspring of thought.  How has this been true for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=22, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=23, question='How does Napoleon Hill define Auto-Suggestion?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=24, question='How much control do you have over the material that reaches your mind?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=25, question='How diligent are you in protecting the "garden of your mind" from negative thoughts?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=26, question='What do you need to add to the words (auto-suggestion) to make your subconscious mind recognize and act upon them?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=27, question='Be on the alert of the plans that your subconscious mind will have over to you and when they appear,  put them into action immediately.  What is an example of taking action immediately on a plan or an idea that has come into your mind?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=28, question='What will happen if you follow some of the instruction of auto-suggestion but not others?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 4,question_number=29, question='How can you become the master of yourself and your environment?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=30, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=31, question='What kinds of specialized knowledge do you have? What kinds of specialized knowledge would help you go to another level?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=32, question='How many kinds of specialized knowledge can you think of beyond those taught in school?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=33, question='How can a Master Mind Group contribute to your specialized knowledge?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=34, question='Those who are not successful usually make the mistake of believing that the knowledge acquiring period ends when one finishes school.  How have you continued to acquire specialized knowledge?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=35, question='Doing a thing well never is trouble!  Do you strive to do everything you do as well as you can?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 5,question_number=36, question='Both success and failure are largely the result of what?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 6,question_number=37, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 6,question_number=38, question='What are the two forms of imagination and how are they unique?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 6,question_number=39, question='What form of imagination will you use to create your goal?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 6,question_number=40, question='What is the beginning point in all fortunes?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 6,question_number=41, question='Success requires no explanation,  failure permits no alibis.  How can that statement inspire you in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=42, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=43, question='What is the Master Mind and why is forming one important?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=44, question='How have you experienced "temporary defeat" in your life?  How have you overcome it?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=45, question='The Major Attributes of Leadership: Which attributes comes naturally to you?  Which attributes are challenging for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=46, question='The Ten Major Causes of Failure in Leadership: Which of these causes can you identify with?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=47, question='The Thirty Major Causes of Failure: Which of these causes can you identify with?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=48, question='The twenty-eight questions title "Take Inventory of yourself - Take some time with a partner or close friend and answer these questions together')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 7,question_number=49, question='How has reviewing the 4 major lists, Attributes, Causes of Failure,  Failure in Leadership and Personal inventory, give you more self-awareness?  What did you learn about yourself? How can that knowledge help you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 8,question_number=50, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 8,question_number=51, question='What is the opposite of decision?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 8,question_number=52, question='Are you someone who reaches decisions quickly and then changes your mind slowly?  How does that impact your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 8,question_number=53, question='How influenced by the opinions of others are you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 8,question_number=54, question='Tell the world what you intend to do but first show it!  How can you apply this to your life and pursuit of your goals?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=55, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=56, question='What is the basis of persistence?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=57, question='If you find yourself lacking in persistence,  this weakness may be remedies by building a stronger fire under your desires.  How can building a stronger fire under your desires help to overcome a lack of persistence?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=58, question='How can a Master Mind help you in building your persistence?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=59, question='Do you have a "poverty consciousness" of a "money consciousness"?  Why?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=60, question='How many of the Symptoms in the Symptoms of lack of persistence can you identify with?  How do you identify with them?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 9,question_number=61, question='What are the four step to developing persistence?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 10,question_number=62, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 10,question_number=63, question='How is "power" defined by Napoleon Hill?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 10,question_number=64, question='What are the "sources of knowledge"?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 10,question_number=65, question='How can you gain power through a Master Mind?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=66, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=67, question='What does Napoleon Hill mean by Sex Transmutation?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=68, question='What are the "Ten Mind Stimuli"?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=69, question='What is the "sixth sense" and how does it develop genius?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=70, question='Where do ideas of "hunches" come from?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=71, question='How would Dr. Elmer R. Gates "sit for ideas".  How can you do this in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 11,question_number=72, question='No man can avail himself of the forces of his creative imagination while dissipating them.  How have you dissipated rather than used your creative forces in the past?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=73, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=74, question='What is the subconscious mind and how does it affect your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=75, question='How can you plant a plan, desire, or purpose into your subconscinous mind?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=76, question='What is it important to guard your mind from negative thoughts?  How do you do that?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=77, question='Why do negative emotions enter our thought impulses voluntarily while positive ones must be injected?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=78, question='What are the Seven Major Positive Emotions and the Seven Major Negative emotions?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 12,question_number=79, question='Positive and negative emotions can occupy the mind at the same time.  Which is your mind filled more with - positive or negative emotions?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 13,question_number=80, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 13,question_number=81, question='Why does Napoleon Hill call the brain "both a broadcasting and receiving station for the vibrations of thought"?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 13,question_number=82, question='In regards to the "Method of mind stimulation,  through discussion of definite subjects between members of the Master Mind,  how have you experienced this in your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=83, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=84, question='How does Napoleon Hill describe the ‘sixth sense" and how it can work on your life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=85, question='Infinite Intelligence,  how is this term used and what does it mean?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=86, question='What is an Imaginary Council and how did it affect the author’s life?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=87, question='If you were to form an imaginary council,  whom would you invite to be in it?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 14,question_number=88, question='How might an imaginary Council aid you in obtaining your goal or desire?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=89, question='What is the most helpful idea from this chapter for you?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=90, question='What are the six ghosts of fear?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=91, question='What is the seventh basic evil?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=92, question='Which of these do you identify with the most?How do you protect yourself against negative influences?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=93, question='Self-Analysis Test Questionss: What did you find most surprising in your answers?')
		Post.objects.get_or_create(user=kwargs.get('instance'), chapter = 15,question_number=94, question='Fifty-Seven Famous Alibis: Which ones have you used the most frequently to limit your own potential?')








