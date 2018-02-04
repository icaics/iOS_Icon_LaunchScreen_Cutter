# iOS Icon LaunchScreen Cutter

### Target

- Resize and resave iOS icon and launchscreen image automatically.

### Result

- ICON:

		20@1x, iPadPro@2x
    	60@1x, 60@2x, 60@3x
    	76@1x, 76@2x, 76@3x
    	29@1x, 29@2x, 29@3x
    	40@1x, 40@2x, 40@3x

- LAUNCHSCREEN:

		640x960
    	640x1136
    	750x1334
    	768x1024
    	1125x2463
    	1242x2208
    	1536x2048

### How to use

- [Pillow](https://github.com/python-pillow/Pillow) required

- Prepare `icon.png` and `launch.png` with `Cutter.py`

- `icon.png` size: **1024x1024**

- `launch.png` size: **2048x2732**

- run `python3 Cutter.py`
