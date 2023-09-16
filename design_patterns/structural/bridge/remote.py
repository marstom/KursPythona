from device import Device


class Remote:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 1)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 1)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedRemote(Remote):
    def mute(self):
        self._device.set_volume(0)

