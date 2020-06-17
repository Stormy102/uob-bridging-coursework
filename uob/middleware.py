

class SecurityHeaders:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Xss-Protection'] = "1; mode=block"
        response['Referrer-Policy'] = "strict-origin"
        response['Feature-Policy'] = "accelerometer 'none'; camera 'none'; fullscreen 'none'; geolocation 'none'; " \
                                     "gyroscope 'none'; magnetometer 'none'; microphone 'none'; payment 'none'; " \
                                     "usb 'none'"
        response['Server'] = 'cloudflare'
        return response
