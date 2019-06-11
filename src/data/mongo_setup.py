import mongoengine


def global_init():
    mongoengine.register_connection(alias='businessapp', name='com_chay')
    mongoengine.connect('Cluster0', host='mongodb+srv://Kpm:Imtrash123@cluster0-y4fz5.mongodb.net/test?retryWrites=true&w=majority')
