#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

COMMON_PATH := device/mediatek/mt8189-common

$(call inherit-product, $(SRC_TARGET_DIR)/product/generic_ramdisk.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/emulated_storage.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/virtual_ab_ota/launch_with_vendor_ramdisk.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/virtual_ab_ota/vabc_features.mk)
$(call inherit-product, hardware/mediatek/overlay/mssi.mk)
$(call inherit-product, hardware/lineage/compat/frameworks/compat.mk)
$(call inherit-product, hardware/mediatek/frameworks/mediatek-frameworks.mk)

# A/B
AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_system=true \
    POSTINSTALL_PATH_system=system/bin/otapreopt_script \
    FILESYSTEM_TYPE_system=ext4 \
    POSTINSTALL_OPTIONAL_system=true

AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_vendor=true \
    POSTINSTALL_PATH_vendor=bin/checkpoint_gc \
    FILESYSTEM_TYPE_vendor=erofs \
    POSTINSTALL_OPTIONAL_vendor=true

PRODUCT_PACKAGES += \
    checkpoint_gc \
    otapreopt_script

PRODUCT_PACKAGES += \
    update_engine \
    update_engine_sideload \
    update_verifier

PRODUCT_PACKAGES_DEBUG += \
    update_engine_client

# VNDK
PRODUCT_PACKAGES += \
    vndservicemanager

# Audio
PRODUCT_PACKAGES += \
    android.hardware.audio.effect@7.0-impl \
    android.hardware.audio.service.mediatek

PRODUCT_PACKAGES += \
    audio.bluetooth.default \
    audio_policy.stub \
    audio.r_submix.default \
    audio.usb.default

# Bluetooth
PRODUCT_PACKAGES += \
    android.hardware.bluetooth-service.default

# Boot control
PRODUCT_PACKAGES += \
    android.hardware.boot-service.mediatek \
    android.hardware.boot-service.mediatek_recovery

# Chipinfo
PRODUCT_PACKAGES += \
    chipinfo

# DRM
PRODUCT_PACKAGES += \
    android.hardware.drm-service.clearkey

# Health
PRODUCT_PACKAGES += \
    android.hardware.health-service.mediatek \
    android.hardware.health-service.mediatek-recovery

# HIDL
PRODUCT_PACKAGES += \
    android.hidl.allocator@1.0-service \
    android.hidl.memory@1.0-impl \
    android.hidl.memory@1.0-impl.vendor \
    hwservicemanager

# Memtrack
PRODUCT_PACKAGES += \
    android.hardware.memtrack-service.mediatek

# Sensors
PRODUCT_PACKAGES += \
    android.hardware.sensors-service.multihal

# Thermal
PRODUCT_PACKAGES += \
    android.hardware.thermal-service.mediatek

PRODUCT_COPY_FILES += \
    $(COMMON_PATH)/configs/thermal/thermal_info_config.json:$(TARGET_COPY_OUT_VENDOR)/etc/thermal_info_config.json

# Partitions
PRODUCT_USE_DYNAMIC_PARTITIONS := true

# Permissions
PRODUCT_PACKAGES += \
    android.hardware.audio.low_latency.prebuilt.xml \
    android.hardware.bluetooth.prebuilt.xml \
    android.hardware.bluetooth_le.prebuilt.xml \
    android.hardware.faketouch.prebuilt.xml \
    android.hardware.touchscreen.multitouch.distinct.prebuilt.xml \
    android.hardware.usb.accessory.prebuilt.xml \
    android.hardware.usb.host.prebuilt.xml \
    android.hardware.wifi.direct.prebuilt.xml \
    android.hardware.wifi.passpoint.prebuilt.xml \
    android.hardware.wifi.prebuilt.xml \
    android.software.device_id_attestation.prebuilt.xml \
    android.software.ipsec_tunnels.prebuilt.xml \
    android.software.verified_boot.prebuilt.xml

# Rootdir
PRODUCT_PACKAGES += \
    fstab.enableswap \
    fstab.mt8391 \
    fstab.mt8391.vendor_ramdisk \
    init.cgroup.rc \
    init.mt8391.rc \
    init.mt8189.usb.rc \
    init.mtkgki.rc \
    init.project.rc \
    init.pstore.rc \
    init.recovery.mt8391.rc \
    init.sensor_2_0.rc \
    ueventd.mt8189.rc

# USB
$(call soong_config_set_bool,mediatek_gadget,use_custom_usb_gadget_rc,true)

# Wi-Fi
PRODUCT_PACKAGES += \
    android.hardware.wifi-service \
    conninfra_loader \
    hostapd \
    libwifi-hal-wrapper \
    wlan_assistant \
    wpa_supplicant

$(call soong_config_set_bool,mediatek_wifi_hal,use_pre_u_qpr2_struct,true)
$(call soong_config_set_bool,mediatek_wifi_hal,use_pre_baklava_qpr0_struct,true)

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    device/mediatek/mt8189-common \
    hardware/google/interfaces \
    hardware/google/pixel/pixelstats \
    hardware/mediatek

$(call inherit-product, vendor/mediatek/mt8189-common/mt8189-common-vendor.mk)
