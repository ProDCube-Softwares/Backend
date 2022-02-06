from typing import Callable

from fastapi import FastAPI


class Utils:

    @staticmethod
    def updateSchemaName(app: FastAPI, function: Callable, name: str) -> None:
        for route in app.routes:
            paths = route.__dict__
            if "endpoint" in paths.keys() and paths["endpoint"] is function:
                route.__dict__["body_field"].type_.__name__ = name
                break
