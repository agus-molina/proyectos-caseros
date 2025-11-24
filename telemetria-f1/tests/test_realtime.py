from livef1.adapters.realtime_client import RealF1Client

client = RealF1Client(
    topics=["Heartbeat", "SessionInfo"]
)

@client.callback("hb")
async def hb(records):
    print("Heartbeat:", records)

@client.callback("info")
async def info(records):
    print("SessionInfo:", records)

client.run()