import pytest

from labgrid.driver.fake import FakeCommandDriver, FakeFileTransferDriver
from labgrid.external import USBStick


class TestUSBStick:
    def test_create(self, target):
        d = FakeCommandDriver(target)
        f = FakeFileTransferDriver(target)
        u = USBStick(target, 'imagepath', 'imagename')
        assert (isinstance(u, USBStick))
