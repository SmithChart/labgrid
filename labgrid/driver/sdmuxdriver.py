import attr

from labgrid.factory import target_factory
from labgrid.driver.common import Driver
from labgrid.protocol import SdmuxProtocoll
from labgrid.resource import SdmuxPort

@target_factory.reg_driver
@attr.s(cmp=False)
class SdmuxDriver(Driver, SdmuxProtocoll):
    bindings = {"sg": SdmuxPort }

    def off(self):
        print("Switching sdmux off")

    def host(self):
        print("Switching to host")

    def dut(self):
        print("Switching to DUT")
