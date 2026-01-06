import Pyro4

@Pyro4.expose
class Chain(object):
    def __init__(self, name, current_server):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None

    # Existing chain forwarding
    def process(self, message):
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        if self.name in message:
            print("Back at %s; the chain is closed!" % self.name)
            return ["complete at " + self.name]
        else:
            print("%s forwarding the message to the object %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "passed on from " + self.name)
            return result

    # New method: reverse a string and check palindrome
    def reverse_and_check_palindrome(self, s):
        reversed_s = s[::-1]
        is_palindrome = s == reversed_s
        return reversed_s, is_palindrome
