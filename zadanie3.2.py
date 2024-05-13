import time

class HTTPRequestHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if not self.can_handle_request(request):
            if self.successor is not None:
                self.successor.handle_request(request)
        else:
            self.process_request(request)

    def can_handle_request(self, request):
        return False

    def process_request(self, request):
        pass

class UserPermissionHandler(HTTPRequestHandler):
    def can_handle_request(self, request):
        return request.user.has_permission(request.type)

    def process_request(self, request):
        print("Użytkownik {} ma odpowiednie uprawnienia.".format(request.user))

class FileCheckHandler(HTTPRequestHandler):
    def can_handle_request(self, request):
        return not request.type == 'file'

    def process_request(self, request):
        print("Żądanie nie dotyczy pliku.")

class RateLimitHandler(HTTPRequestHandler):
    def __init__(self, rate_limit_per_minute, successor=None):
        super().__init__(successor)
        self.rate_limit_per_minute = rate_limit_per_minute
        self.requests_count = 0
        self.last_reset_time = time.time()

    def can_handle_request(self, request):
        now = time.time()
        if now - self.last_reset_time >= 60:
            self.requests_count = 0
            self.last_reset_time = now
        self.requests_count += 1
        return self.requests_count <= self.rate_limit_per_minute

    def process_request(self, request):
        print("Liczba żądań na minutę nie została przekroczona.")

class SQLInjectionCheckHandler(HTTPRequestHandler):
    def can_handle_request(self, request):
        return "sql" not in request.data.lower()

    def process_request(self, request):
        print("Brak próby SQL Injection w przesłanych danych.")


class HTTPRequest:
    def __init__(self, user, type, data):
        self.user = user
        self.type = type
        self.data = data

user = "example_user"
type = "GET"
data = "SELECT * FROM users"
request = HTTPRequest(user, type, data)

handler = UserPermissionHandler(
            FileCheckHandler(
                RateLimitHandler(100, 
                    SQLInjectionCheckHandler())))

handler.handle_request(request)
