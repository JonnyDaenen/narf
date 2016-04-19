
import logging

class NarfAgent:

    _service_manager = None
    _body = None
    _id = None


    def __init__(self, id, servicemanager):
        self._service_manager = servicemanager
        self._id = id


    def _get_environment(self):
        return self.__get_service("ENVIRONMENT")

    def _get_whitepages(self):
        return self.__get_service("WHITEPAGES")

    def _get_clock(self):
        return self.__get_service("CLOCK")

    def _get_spawner(self):
        return self.__get_service("SPAWNER")

    def _get_gps(self):
        return self.__get_service("GPS")


    def get_id(self):
        pass


    def start(self):
        pass
        environment = self._get_environment()
        _body = environment.request_body(self)
        logging.info("Agent %s Requested body"%self._id)
        #request body



    def do_step(self):
        pass


    def stop(self):
        pass
        #release body


    def __kill(self):
        pass
        #remove from whitepages


    def __get_service(self, name):
        return self._service_manager.get_service_supplier(name)


    def __get_time(self):
        return self._get_clock().get_time()


