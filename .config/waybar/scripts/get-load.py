import psutil
import time

def current_net_load(interval=1.0):
    a = psutil.net_io_counters()
    time.sleep(interval)
    b = psutil.net_io_counters()
    sent_per_sec = (b.bytes_sent - a.bytes_sent) / interval
    recv_per_sec = (b.bytes_recv - a.bytes_recv) / interval

    return recv_per_sec, sent_per_sec

if __name__ == "__main__":
    down_bps, up_bps = current_net_load(1.0)
    down_mbs = down_bps / 1048576
    up_mbs = up_bps / 1048576
    print(f" {down_mbs:.2f} MB/s  {up_mbs:.2f} MB/s")