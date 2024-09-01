import aiohttp
import asyncio
from itertools import count
async def send_post_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            print("Post async")
            return await response.text()
'''
async def main():
    url = 'http://192.168.50.193:5869/post_data'
    data = {
        'key': 'value'
    }
    
    # Send POST request without using a for loop
    response_text = await send_post_request(url, data)
    print(response_text)
'''
async def main():
    #url = 'http://192.168.50.193:5869/post_data'
    url = 'https://roboreactor.com/feedback_sensor'
    #data_list = [{'key': 'value1'}, {'key': 'value2'}, {'key': 'value3'}]
    #tasks = [send_post_request(url, data) for data in data_list]
    #responses = await asyncio.gather(*tasks)
    
    for i in count(0):
       for rc in range(0,241,1):
            data = {'kornbot380@hotmail.com':{'wrist':{'Analog-read':rc},'shoulder':{'Analog-read':rc},'base':{'Analog-read':rc}}} 
            response_text = await send_post_request(url, data)
            print(response_text)
       for rc in range(241,0,-1):
            data ={'kornbot380@hotmail.com':{'wrist':{'Analog-read':rc},'shoulder':{'Analog-read':rc},'base':{'Analog-read':rc}}} 
            response_text = await send_post_request(url, data)
            print(response_text)
 
# Run the asyncio event loop
asyncio.run(main())
