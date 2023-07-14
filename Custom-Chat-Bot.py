import re
import random

class RuleBot:
    #Potential negative responses
    negative_responses=('no', 'nope', 'not a change', 'sorry', 'nah', 'naw' )
    
    #exit conversation keywords
    exit_commands=('quit', 'pause', 'goodbye', 'bye', 'later', 'pause', 'exit')
    
    #Random starter questions
    random_questions=('Why are you here?', 'Are there many humans like you?',
                      'What do you consume for sustenance?',
                      'Is there intelligent life on this planets?',
                      'Does Earth have a leader?', 'What planets have you visited?', 
                      'What technology do you have on this planet?')
    
    #constructor
    
    def __init__(self) -> None:
        self.alienbabble={
            'describe_planet_intent':r'.*\s*your planet.*',
            'answer_why_intent':r'why\sare.*',
            'about_intellipat':r'.*\sintellipaat'
        }
        
    def greet(self):
        self.name=input("What is your name?\n")
        will_help=input(
            f'Hi {self.name}, I am Rule Bot. Will you help me learn about your planet?\n'
        )
        
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return 
        self.chat()
        
        #Method for exiting the program
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print('Okay, Have a nice Earth day!')

                return True
        #Method for chatting with the bot
    def chat(self):
        reply=input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply=input(self.match_reply(reply))
            
          #Method to reply to the bot  
    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent=key
            regex_pattern=value
            found_match=re.match(regex_pattern, reply)
            
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent =='about_intellipat':
                return self.about_intellipat()
            
        if not found_match:
            return self.no_match_intent()
        
    def describe_planet_intent(self):
        responses=('My planet is a utopia of divers organism and species.\n',
                   'I am from Opidipus, the capital of the keyword Galaxies.\n')
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses=('I come in peace\n', 
                   'I am here to collect data about your planet and its inhabitants.\n',
                   'I heard the coffee is good\n')
    def about_intellipat(self):
        responses=("Intellipaat is world's largest professional educational company.\n", 'Intellipaat will make you learn concepts in the never forget.\n',
                   'Intellipaat is where your career and skills grows.\n')  
        return random.choice(responses)
    
    def no_match_intent(self):
        responses=(
            'Please tell me more.\n', 'Tell me more!\n', 'Why do you say that?\n', 'I see. Can you elaborate?\n',
            'Interesting. Can you tell me more?\n', 'I see. How do you think?\n', 'Why?\n',
            'How do you think I feel you say that?\n'
        )
        
        return random.choice(responses)
    

AllienBot=RuleBot()
AllienBot.greet()    