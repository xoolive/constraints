from . import tiny as tiny_instance
from . import small as small_instance
from . import normal as normal_instance

__all__ = ["tiny", "small", "normal"]

instances = {
    "tiny": tiny_instance,
    "small": small_instance,
    "normal": normal_instance,
}


def get_instance(name: str):
    module = instances[name]
    return dict(
        (key, getattr(module, key))
        for key in dir(module)
        if not key.startswith("_")
    )


tiny = get_instance("tiny")
small = get_instance("small")
normal = get_instance("normal")
