import attr

from ..factory import target_factory
from .common import Resource, NetworkResource


@target_factory.reg_resource
@attr.s(cmp=False)
class SdmuxPort(Resource):
    """The Sdmux describes a locally connected USB-SD-Mux

    Args:
        sg (str):
    """
    sg = attr.ib(validator=attr.validators.instance_of(str))

@target_factory.reg_resource
@attr.s(cmp=False)
class NetworkSdmuxPort(NetworkResource):
    """The Sdmux describes a locally connected USB-SD-Mux

    Args:
        sg (str):
        command (str):
    """
    sg = attr.ib(validator=attr.validators.instance_of(str))
    command = attr.ib(default="usbsdmux", validator=attr.validators.instance_of(str))
