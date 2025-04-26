from flask import Request

def is_mobile(request: Request):
    if request.user_agent.string.find("Mobile") == -1:
        return False
    else:
        return True