#!/usr/bin/env bash

python "imei.py"

emulator -avd $1 -system images/system.img -ramdisk images/ramdisk.img -wipe-data -prop dalvik.vm.execution-mode=int:portable &
