config = {
    "token" : "yourtoken",
    "color" : 0x86E57F,
    "error" : 0xFF0000,
    "nice" : 0xABF200
}
import datetime
def now_time():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')
