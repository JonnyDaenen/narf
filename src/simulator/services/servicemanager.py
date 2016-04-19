


class ServiceManager:

    def __init__(self):
        self.index = {}


    def register_service(self, name, service):
        self.index[name] = service

    def unregister_service(self, name):
        self.index[name] = None
        # TODO remove

    def get_service_supplier(self, name):
        return self.index[name]

    def get_service_names(self):
        return self.index.keys()



