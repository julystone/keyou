import websocket


class WebSApp:

    def on_message(self, ws, message):  # 服务器有数据更新时，主动推送过来的数据
        print(message)

    def on_error(self, ws, error):  # 程序报错时，就会触发on_error事件
        print(error)

    def on_close(self, ws):
        print("Connection closed ……")

    def connect(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://10.0.2.236:28000/platform/api/websocket/admin",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)

        ws.run_forever(ping_timeout=30)


web = WebSApp()
web.connect()
