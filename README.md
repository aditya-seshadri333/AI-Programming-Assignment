Aditya Seshadri- se24ucse012

1.Turing Test Architecture:
The Turing Test is used to determine whether a machine can imitate human intelligence in conversation.

Components:
1. User Interface – chat window where conversation happens
2. Human Judge – evaluates the conversation
3. AI Chatbot – machine that tries to behave like a human
4. Conversation Manager – controls the flow of messages
5. Decision Module – judge decides if responses are human or machine

System Flow:
User → Chat Interface  
Chat Interface → Conversation Manager  
Conversation Manager → AI Chatbot  

The judge reads the conversation and decides:

Human OR Machine

Architecture Diagram:
User  
↓  
Chat Interface  
↓  
Conversation Manager  
↓  
AI Chatbot  

Judge observes conversation → Final decision

2.CAPTCHA Archictecture:
CAPTCHA is used to distinguish humans from bots on websites.

Components:
1. Web Server
2. CAPTCHA Generator
3. Distortion Engine
4. CAPTCHA Image
5. Validation Module
6. Database

System Flow:
User requests webpage  
↓  
Server generates CAPTCHA  
↓  
Distorted image is shown to the user  
↓  
User enters the text  
↓  
Validation module checks the answer  
↓  
Access Granted / Access Denied

Architecture Diagram:
User  
↓  
Website Server  
↓  
CAPTCHA Generator  
↓  
Distorted Image  

User enters answer  
↓  
Validation Module  
↓  
Access granted or denied
