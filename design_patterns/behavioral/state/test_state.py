from state import *


def test_ctx():
    print()
    engine = EngineContext(OffState())
    engine.push_on_off()

    opts = Options(voltage=121, password="psd")
    engine.set_options(opts)
    opts.voltage = 22
    engine.set_options(opts)

    engine.set_speed(2500)
    # off engine
    engine.push_on_off()

    # again, start from the beginning and conduct test procedure
    engine.push_on_off()




