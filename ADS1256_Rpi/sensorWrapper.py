import random
import time

import websockets
import asyncio
import json

import ADS1256

import RPi.GPIO as GPIO, time, os    

async def listen():
    url = 'ws://192.168.0.102:7891'

    # Connect to our websocket server
    async with websockets.connect(url) as ws:
        try:
            # stay alive forever to incoming messages
            # await ws.send("Connected!")
            while True:
                print("In Loop")
                time.sleep(2)
                #await ws.send(str(random.randint(0, 10)))  # Replace 'random.randint(0, 10)' with the sensor function.
        except websockets.exceptions.ConnectionClosedError as error1:
            print(f"Client Error: {error1}")


async def my_function():
    url = 'ws://192.168.0.102:7891'
    data = []
    async for websocket in websockets.connect(url):
        while True:
            try:
                data = str(random.randint(0, 10))
                ADC = ADS1256.ADS1256()
                ADC.ADS1256_init()
                ADC_Value = ADC.ADS1256_GetAll()
                data1 = (ADC_Value[0]*5.0/0x7fffff)
                data2 = (ADC_Value[1]*5.0/0x7fffff)
                data3 = (ADC_Value[2]*5.0/0x7fffff)
                data4 = (ADC_Value[3]*5.0/0x7fffff)
                data5 = (ADC_Value[4]*5.0/0x7fffff)
                data6 = (ADC_Value[5]*5.0/0x7fffff)
                data7 = (ADC_Value[6]*5.0/0x7fffff)
                data8 = (ADC_Value[7]*5.0/0x7fffff)
                data = [data1, data2, data3,data4,data5,data6,data7,data8]
                msg = json.dumps([{"channel": i, "data": data[i]} for i in range(0, 8)])
                await websocket.send(msg)
        
                print(data)
                await asyncio.sleep(10)
            except websockets.ConnectionClosed as e:
                print(f'Terminated: {e}')


# Start the connection
asyncio.run(my_function())
