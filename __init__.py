from .nodes.batchcrop_nodes import ADBatchCropFromMaskAdvanced, ADBatchUncropAdvanced

NODE_CLASS_MAPPINGS = {
    "ADBatchCropFromMaskAdvanced": ADBatchCropFromMaskAdvanced,
    "ADBatchUncropAdvanced": ADBatchUncropAdvanced,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ADBatchCropFromMaskAdvanced": "AD CropFit Advanced",
    "ADBatchUncropAdvanced": "AD UncropFit Advanced",
}

WEB_DIRECTORY = "./web"

from aiohttp import web
from server import PromptServer
from pathlib import Path

if hasattr(PromptServer, "instance"):
    try:
        PromptServer.instance.app.add_routes(
            [
                web.static(
                    "/kjweb_async",
                    (Path(__file__).parent.absolute() / "kjweb_async").as_posix(),
                )
            ]
        )
    except Exception:
        pass

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
