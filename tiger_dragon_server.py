import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print(data)

    def Network_shoot(self, data):
        #player number (1 or 0)
        num = data["num"]
        self.gameid = data["gameid"]
        self._server.shoot(data, self.gameid, num)

    def Network_move(self, data):
        #player number (1 or 0)
        num = data["num"]
        self.gameid = data["gameid"]
        self._server.move(data, self.gameid, num)

    def Network_win(self, data):
        #player number (1 or 0)
        num = data["num"]
        self.gameid = data["gameid"]
        self._server.win(self.gameid, num)
 
class TigerDragonServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.games = []
        self.queue = None
        self.currentIndex = 0
        
    def Connected(self, channel, addr):
        if self.queue == None:
            print("player 0 set:", channel)
            self.currentIndex += 1
            channel.gameid = self.currentIndex
            self.queue = Game(channel, self.currentIndex)
        else:
            print("player 1 set:", channel)
            channel.gameid = self.currentIndex
            self.queue.player1 = channel
            self.queue.player0.Send({"action": "startgame", "player": 0, "gameid": self.queue.gameid})
            self.queue.player1.Send({"action": "startgame", "player": 1, "gameid": self.queue.gameid})
            self.games.append(self.queue)
            self.queue = None

    def shoot(self, data, gameid, num):
        game = [i for i in self.games if i.gameid == gameid]
        if len(game) == 1:
            game[0].shoot(data, num)

    def move(self, data, gameid, num):
        game = [i for i in self.games if i.gameid == gameid]
        if len(game) == 1:
            game[0].move(data, num)

    def win(self, gameid, num):
        game = [i for i in self.games if i.gameid == gameid]
        if len(game) == 1:
            game[0].win(num)

class Game:
    def __init__(self, player0, currentIndex):
        # whose turn (1 or 0)
        self.turn = 0
        self.player0 = player0
        self.player1 = None
        self.gameid = currentIndex
        
    def shoot(self, data, num):
        #make sure it's their turn
        if num == self.turn:
            self.turn = 0 if self.turn else 1
            self.player0.Send(data)
            self.player1.Send(data)
            self.player0.Send({"action":"yourturn", "turn":True if self.turn == 0 else False})
            self.player1.Send({"action":"yourturn", "turn":True if self.turn == 1 else False})

    def move(self, data, num):
        #make sure it's their turn
        if num == self.turn:
            self.turn = 0 if self.turn else 1
            self.player0.Send(data)
            self.player1.Send(data)
            self.player0.Send({"action":"yourturn", "turn":True if self.turn == 0 else False})
            self.player1.Send({"action":"yourturn", "turn":True if self.turn == 1 else False})

    def win(self, num):
        if num == 0:
            self.player1.Send({"action":"lose"})
        else:
            self.player0.Send({"action":"lose"})
 
print("STARTING SERVER ON LOCALHOST")
server = TigerDragonServer(localaddr=("0.0.0.0", 12345))
while True:
    server.Pump()
    sleep(0.01)
