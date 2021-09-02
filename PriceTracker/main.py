import requests
import time

# list of quotes
quotes = [
    'First, solve the problem. Then, write the code. – John Johnson',
    'Experience is the name everyone gives to their mistakes. – Oscar Wilde',
    'Code is like humor. When you have to explain it, it’s bad. – Cory House',
    'Before software can be reusable it first has to be usable. – Ralph Johnson',
    'Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
]

# loop through the quotes
for quote in quotes:
    url = 'https://api.telegram.org/bot1932360016:AAHV8pU4FPFAHttcLc3Q_kiM1MdmZhBmRb4/sendMessage?chat_id=CHAT_ID&text="{}"'.format(quote)
    requests.get(url)
    # sends new quotes every 20seconds
    time.sleep(5)