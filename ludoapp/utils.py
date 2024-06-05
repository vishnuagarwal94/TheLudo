from django.http import HttpResponseRedirect

class WhatsappRedirect(HttpResponseRedirect):
    allowed_schemes = ['http', 'https', 'ftp', 'ftps', 'mailto', 'whatsapp']