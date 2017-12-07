import attr
import subprocess
import logging

from labgrid.factory import target_factory
from labgrid.driver.common import Driver
from labgrid.protocol import SdmuxProtocol
from labgrid.resource import SdmuxPort, NetworkSdmuxPort

@target_factory.reg_driver
@attr.s(cmp=False)
class SdmuxDriver(Driver, SdmuxProtocol):
    bindings = {"sdmuxport": {SdmuxPort, NetworkSdmuxPort} }

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.logger = logging.getLogger("{}({})".format(self, self.target))

    @Driver.check_active
    def off(self):
        self._exec("off")

    @Driver.check_active
    def host(self):
        self._exec("host")

    @Driver.check_active
    def dut(self):
        self._exec("dut")

    @Driver.check_active
    def _exec(self, target):
        print("Switching sdmux {} to: {}".format(self.sdmuxport.sg, target))
        self.logger.debug("Switching sdmux {} to: off".format(self.sdmuxport.sg))

        args = "usbsdmux -c {} off".format(self.sdmuxport.sg).split(" ")

        if isinstance(self.sdmuxport, SdmuxPort):
            proc = subprocess.check_call(args)
        elif isinstance(self.sdmuxport, NetworkSdmuxPort):
            proc = subprocess.check_call(self.sdmuxport.command_prefix + args)

