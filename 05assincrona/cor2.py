import asyncio

async def diz_oi_demoradi():
    print("Oi...")
    await asyncio.sleep(2)
    print("Todos...")


el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demoradi())
el.close()