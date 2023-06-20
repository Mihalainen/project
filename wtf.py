import request

kit_header = ("Bearer" + request.response_token)
print(kit_header)