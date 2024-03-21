import json
import argparse
import sys
from typing import Optional


def load_base_capability():
    with open('appium.json') as f:
        config = json.load(f)
    return {**config['base_capability']}


def load_capabilities():
    with open('appium.json') as f:
        config = json.load(f)
    return config['capabilities']


def get_appium_server_url() -> str:
    with open('appium.json') as f:
        config = json.load(f)
    return config['server']['url']


def get_target_devices_from_args() -> list[str]:
    """
    讀取指令取得指定 devices
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--devices', nargs='?', default=None)
    args = parser.parse_args(sys.argv[1:])
    return args.devices.split(',') if args.devices else []


def get_device_capability():
    device_capabilities = load_capabilities()
    devices = get_target_devices_from_args()

    target_capability: Optional[dict] = None
    if devices is not None:
        for capability in device_capabilities:
            if capability['deviceName'] == devices:
                target_capability = capability
                break
    if target_capability is None:
        target_capability = device_capabilities[0]

    target_capability = {
        **load_base_capability()[target_capability['platformName']],
        **target_capability,
    }

    return target_capability
