from device import Device, Radio, TV
from remote import AdvancedRemote, Remote


def print_device_info(device: Device):
    print(f"""
    Device type:{type(device)}
    enabled: {device.is_enabled()}
    vol:     {device.get_volume()}
    channel: {device.get_channel()}
    """)


def test_remote():
    tv = TV()
    radio = Radio()
    remote_tv = Remote(tv)
    remote_tv.toggle_power()
    [remote_tv.volume_up() for _ in range(200)]

    print_device_info(tv)

    assert tv.get_volume() == 10

    [remote_tv.volume_down() for _ in range(200)]
    assert tv.get_volume() == 0

    remote_radio = Remote(radio)
    [remote_radio.volume_up() for _ in range(200)]
    assert radio.get_volume() == 100


    adv_radio_remote = AdvancedRemote(radio)
    adv_radio_remote.mute()
    assert radio.get_volume() == 0
