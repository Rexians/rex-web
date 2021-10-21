import speedtest

st = speedtest.Speedtest()

class speed:
    def __init__(self):
        st.get_servers()
        best = st.get_best_server()
        speed_dict = st.results.dict()
        self.download = (speed_dict['download']) #/1024/1024:.2f
        self.upload = (speed_dict['upload'])
        self.ping = (speed_dict['ping'])
        self.host_info = (f"{best['host']} located in {best['country']}")
        self.ip = (speed_dict['client']['ip'])

    def downloads(self):
        return {self.download}
    def uploads(self):
        return self.upload
    def pings(self):
        return self.ping
    def host_infos(self):
        return self.host_info
    def ips(self):
        return self.ip                
