import asyncio
import aiohttp
import time


def menu():
 print('--------------------*Check status manually*')
 print('')
 print('--1=Choose website to fetch ')
 print('--2=View urls')
 print('--3=view line by line status ')
 print('--4= Exit program')
 print('')
 print('---------------------To go back press *back*')
x=menu()
urls=[]
status=[]
while True:
 choose=int(input('Enter value :'))

 match choose:
    case 1:
       
        print('Check status website')
        while True:
         url=input(f'Enter the URL or press *back* to back :')
         urls.append(url)
         if url=='back':
            print('you are successfully back ')
            break

         else:
            async def wrapper(url):
               async with aiohttp.ClientSession() as session:
                  async with session.get(url) as response:
                     print(f"The response of website is {response.status}")
                     status.append(response.status)
            async def main():
               start=time.time()
               await asyncio.gather(wrapper(url))
               end=time.time()
               print(f'Total time taken to fetch and get {end-start:.2f}seconds ')
            asyncio.run(main())
            
    case 2:
      print('The URls are :')
      for i in urls:
         print(i)
    case 3:
       for x,y in zip(status,urls):
          print(f'URL :{y} , Response status :{x}')

    case _:
       print("You have been exited successfully !")



         
    

      
        
            
        
         




