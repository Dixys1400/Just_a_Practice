import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = test.donwload()
    down_speed = round(down_speed / 10**6, 2)
    print("Donwload Speed in Mbps:", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10*6, 2)
    print("Upload Speed in Mbps:", up_speed)

    ping = test.result.ping
    print("Ping:", ping)
Speed_Test()


