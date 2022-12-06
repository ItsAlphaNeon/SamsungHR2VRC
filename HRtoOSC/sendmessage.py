from pythonosc.udp_client import SimpleUDPClient


def sendHeartRate(heartrate):
    ip = "127.0.0.1"  # LocalHost
    port = 9000  # VRChat Port
    parseHR = int(heartrate)
    client = SimpleUDPClient(ip, port)  # Create client

    client.send_message("/avatar/parameters/HeartRate", parseHR)  # Send message with int, float and string
    print("Sent the value {} to vrc".format(parseHR))
