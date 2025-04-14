from .abc import AbstractCommand


class LicenseCommand(AbstractCommand):
    name = "license"

    def configure_parser(self, subparsers):
        parser = subparsers.add_parser(self.name)
        parser.set_defaults(handler=self.main)

    def main(self):
        pass
