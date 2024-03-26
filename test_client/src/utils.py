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


def get_appium_server_urls() -> list[str]:
    with open('appium.json') as f:
        config = json.load(f)
    return config['server']['urls']


def get_target_devices_from_args() -> list[str]:
    """
    讀取指令取得指定 devices
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--devices', nargs='?', default=None)
    args = parser.parse_args(sys.argv[1:])
    return args.devices.split(',') if args.devices else []


def get_device_capabilities():
    device_capabilities = load_capabilities()
    target_devices = get_target_devices_from_args()

    if target_devices is None:
        return []

    target_capabilities = []
    for capability in device_capabilities:
        if capability['id'] in target_devices:
            target_capabilities.append({
                **load_base_capability()['Common'],
                **load_base_capability()[capability['platformName']],
                **capability
            })

    # 這個寫法同上面，但感覺比較難讀
    # target_capabilities = [
    #     {
    #         **load_base_capability()['Common'],
    #         **load_base_capability()[capability['platformName']],
    #         **capability
    #     } for capability in device_capabilities if capability['id'] in target_devices
    # ]

    return target_capabilities
