# Test Client

## Get Started

```shell
brew install allure
```

### iOS

```shell
appium driver install xcuitest
```

### Setup

- 根據 `appium_sample.json` 建立 `appium.json`

## Notes

### Capabilities

Android

- `deviceName`: 透過指令 `adb devices` 取得
- `platformVersion`: Android 版本，透過指令 `adb shell getprop ro.build.version.release` 取得
- `platformName`: `Android`

### 指定 Capabilities

![](screenshots/setup_capabiity_params_1.png)

![](screenshots/setup_capabiity_params_2.png)

## References

- [PyTest Testing Framework](https://www.youtube.com/playlist?list=PLsjUcU8CQXGECu4Sl1IwrguGRU0iQGt3E)
