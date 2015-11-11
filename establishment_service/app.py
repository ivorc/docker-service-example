from tornado.ioloop import IOLoop
from tornado.web import Application, url
from establishment_handler import EstablishmentHandler
from establishment_repository import EstablishmentRepository


def make_app():
    return Application(get_handlers())


def get_handlers():
    return [
        url(r"/establishment/?", EstablishmentHandler, dict(establishment_repository=EstablishmentRepository())),
        url(r"/establishment/(.+)", EstablishmentHandler, dict(establishment_repository=EstablishmentRepository())),
    ]


def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
