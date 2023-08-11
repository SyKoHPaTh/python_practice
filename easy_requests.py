# ---- Imports ----
import requests # pip install requests


''' API test class

        Handles all communication with the server

        Client                                  Server

        Request-> send post/get/put/delete
                                        code&data<-Response

    Requests: https://docs.python-requests.org/en/latest/user/quickstart/
        r = requests.get('https://httpbin.org/put', data={'key': 'value'})
        r = requests.post('https://httpbin.org/put', data={'key': 'value'})
        r = requests.put('https://httpbin.org/put', data={'key': 'value'})
        r = requests.delete('https://httpbin.org/delete')
        r = requests.head('https://httpbin.org/get')
        r = requests.options('https://httpbin.org/get')

'''
class API(object):

    def __init__(self):
        super().__init__()

        self.ping = 0

        self.server_url = 'https://httpbin.org/'

        self.error = ''

    def response_status(self, code, message_error):
        error_message = 'Unknown Response: ' + str(code) + str(message_error)

        # 200's we're basically good, unless....
        if code == 200: 
            error_message = 'OK'
            if str(message_error) != '':
                error_message = str(message_error)
        # 300's redirection, update the game I guess?
        if code == 301: error_message = 'Redirection'
        # 400's, client problem
        if code == 400: error_message = 'Bad Request'
        if code == 401: error_message = 'Invalid Authentication'
        if code == 403: error_message = 'Forbidden'
        if code == 404: error_message = 'Not found!'
        # 500's, server problem
        if code == 500: error_message = 'Server Error: ' + str(message_error)
        if code == 502: error_message = 'Bad Gateway'
        if code == 503: error_message = 'Server Unavailable: Overloaded or Maintenance: ' + str(message_error)
        if code == 504: error_message = 'Server Timeout'

        return error_message

    # Request/Reponse handler:
        # Page: function name in API, typically: sync, verify, register, login
    def query(self, page, request_type, params):

        attempts = 0
        while attempts < 5:
            try:
                if request_type == 'GET': response = requests.get(self.server_url + page, params=params, timeout=5)
                if request_type == 'POST': response = requests.post(self.server_url + page, params=params, timeout=5)
                if request_type == 'PUT': response = requests.put(self.server_url + page, params=params, timeout=5)
                if request_type == 'DELETE': response = requests.delete(self.server_url + page, timeout=5)
                if request_type == 'HEAD': response = requests.head(self.server_url + page, timeout=5)
                if request_type == 'OPTIONS': response = requests.options(self.server_url + page, timeout=5)
                attempts = 5
            except requests.exceptions.HTTPError as e:
                print('Invalid HTTP response:' + str(e) + "\n")
            except requests.exceptions.ConnectionError as e:
                print('Network problem, unable to connect: ' + str(e) + "\n")
            except requests.exceptions.Timeout:
                print('Timed out, try again=' + str(attempts) + "\n")
                attempts += 1
                if attempts == 5:
                    print('Connection Timed out, unable to reconnect')
                    return {"error": 'Connection Timed out, unable to connect' }
            except requests.exceptions.TooManyRedirects:
                print('Invalid URL' + self.server_url + 'API.php/' + page + "\n")
                return False
            except requests.exceptions.RequestException as e:
                print('Auth::' + str(page) + '() Fatal Error:' + str(e) + "\n")
                self.force_logout = True
                return False

        try:
            # Handle Response

            response_raw = response.raw # Raw socket response: need to allow stream=True in requests, then response.raw.read(length)
            print('Response Raw:', response_raw)

            response_text = response.text # plain text, need to worry about converting to other data structures/types
            print('Response Text:', response_text)

            return_json = response.json() # built-in json decoder; imo easiest to work with
            print('Response Text:', return_json)

            err_mess = ''
            error = self.response_status(response.status_code, err_mess)
        except:
            print("Error: " + str(response) + str(response.text) + "\n")
            error = 'Server Error'

        self.ping = int(response.elapsed.total_seconds() * 1000)

        if error != 'OK':
            return_json = {"error": error }

        return return_json


#==========================

api = API()

parameters = { 'key': 'value', 'text': 'thing'}

success = api.query('post', 'POST', parameters)

print('Response paramters:', success['args'])
print('Ping:', api.ping, 'ms')