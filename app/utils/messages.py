def success_message():
    return {
        'message': 'Success event',
        'code': 200
    }

def success_message_with_data(data):
    return {
        'message': 'Success event',
        'code': 200,
        'data': data
    }

def error_message(error):
    return {
        'message': 'Error when application is executing',
        'code': 500,
        'error': error
    }
