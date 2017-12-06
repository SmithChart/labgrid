import attr

from ..factory import target_factory
from .common import Resource


@target_factory.reg_resource
@attr.s(cmp=False)
class SdmuxPort(Resource):
    """The Sdmux describes a locally connected USB-SD-Mux

    Args:
        sg (str):
    """
    sg = attr.ib(validator=attr.validators.instance_of(str))
