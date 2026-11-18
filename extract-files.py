#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/mediatek/mt8189-common',
    'hardware/mediatek',
]



def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'arm.graphics-V4-ndk',
        'libEGL_angle',
        'libGLES_mali',
        'libGLESv1_CM_angle',
        'libGLESv2_angle',
        'libOpenCL',
        'libarmnn',
        'libgpudataproducer',
        'libion_mtk',
        'libmtkperf_client_vendor',
        'libperfctl_vendor',
        'libpowerhalwrap_vendor',
        'libteec',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/hw/android.hardware.security.keymint@3.0-service.tee': blob_fixup()
        .replace_needed('lib_android_keymaster_keymint_utils.so', 'lib_android_keymaster_keymint_utils-v34.so'),
    (
        'vendor/bin/hw/mt8189/android.hardware.graphics.allocator-V2-service-mediatek.mt8189',
        'vendor/lib/egl/mt8189/libGLES_mali.so',
        'vendor/lib/hw/mt8189/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib/hw/mt8189/android.hardware.graphics.mapper@4.0-impl-mediatek.so',
        'vendor/lib/hw/mt8189/mapper.mediatek.so',
        'vendor/lib/libcodec2_fsr.so',
        'vendor/lib/vendor.mediatek.hardware.pq_aidl-V2-ndk.so',
        'vendor/lib/vendor.mediatek.hardware.pq_aidl-V5-ndk.so',
        'vendor/lib64/egl/mt8189/libGLES_mali.so',
        'vendor/lib64/hw/mt8189/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/hw/mt8189/android.hardware.graphics.mapper@4.0-impl-mediatek.so',
        'vendor/lib64/hw/mt8189/mapper.mediatek.so',
        'vendor/lib64/libaimemc.so',
        'vendor/lib64/libcodec2_fsr.so',
        'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
        'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
        'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V2-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V4-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V5-ndk.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    (
        'vendor/lib/egl/libGLESv2_angle.so',
        'vendor/lib/mt8189/libneuralnetworks_sl_driver_mtk_prebuilt.so',
        'vendor/lib/mt8189/libneuron_adapter_mgvi.so',
        'vendor/lib64/egl/libGLESv2_angle.so',
        'vendor/lib64/mt8189/libneuralnetworks_sl_driver_mtk_prebuilt.so',
        'vendor/lib64/mt8189/libneuron_adapter_mgvi.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .clear_symbol_version('ANativeWindow_getFormat'),
    (
        'vendor/lib/hw/mt8189/vendor.mediatek.hardware.pq_aidl-impl.so',
        'vendor/lib64/hw/mt8189/vendor.mediatek.hardware.pq_aidl-impl.so',
    ): blob_fixup()
        .add_needed('libui_shim.so'),
    (
        'vendor/lib/hw/android.hardware.soundtrigger3-impl.so',
        'vendor/lib64/hw/android.hardware.soundtrigger3-impl.so',
    ): blob_fixup()
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    (
        'vendor/lib/hw/audio.primary.mediatek.so',
        'vendor/lib/hw/mt8189/vendor.mediatek.hardware.pq_aidl-impl.so',
        'vendor/lib/lib_power_applist.so',
        'vendor/lib/libpowerhal.so',
        'vendor/lib/libpqxmlparser.so',
        'vendor/lib/librt_extamp_intf.so',
        'vendor/lib/mt8189/libmmlpqImpl.so',
        'vendor/lib64/hw/audio.primary.mediatek.so',
        'vendor/lib64/hw/mt8189/vendor.mediatek.hardware.pq_aidl-impl.so',
        'vendor/lib64/lib_power_applist.so',
        'vendor/lib64/libpowerhal.so',
        'vendor/lib64/libpqxmlparser.so',
        'vendor/lib64/librt_extamp_intf.so',
        'vendor/lib64/libsilkybrightnesscore.so',
        'vendor/lib64/mt8189/libmmlpqImpl.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    (
        'vendor/lib/hw/vendor.mediatek.hardware.bluetooth.audio@2.1-impl.so',
        'vendor/lib/hw/vendor.mediatek.hardware.bluetooth.audio@2.2-impl.so',
        'vendor/lib/libbluetooth_audio_session_aidl_mtk.so',
        'vendor/lib64/android.hardware.bluetooth.audio-impl-mediatek.so',
        'vendor/lib64/hw/vendor.mediatek.hardware.bluetooth.audio@2.1-impl.so',
        'vendor/lib64/hw/vendor.mediatek.hardware.bluetooth.audio@2.2-impl.so',
        'vendor/lib64/libbluetooth_audio_session_aidl_mtk.so',
    ): blob_fixup()
        .replace_needed('vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so', 'vendor.mediatek.hardware.bluetooth.audio-V2-ndk.so'),
    (
        'vendor/lib/libarmnn_ndk.mtk.vndk.so',
        'vendor/lib64/libarmnn_ndk.mtk.vndk.so',
        'vendor/lib64/mt8189/lib3a.ae.stat.so',
        'vendor/lib64/mt8189/lib3a.flash.so',
        'vendor/lib64/mt8189/lib3a.sensors.color.so',
        'vendor/lib64/mt8189/lib3a.sensors.flicker.so',
    ): blob_fixup()
        .add_needed('liblog.so'),
    (
        'vendor/lib/libcodec2_mtk_vdec.so',
        'vendor/lib/libcodec2_mtk_venc.so',
        'vendor/lib64/libcodec2_mtk_vdec.so',
        'vendor/lib64/libcodec2_mtk_venc.so',
    ): blob_fixup()
        .replace_needed('libformatter.so', 'libformatter_mtk.so'),
    'vendor/lib64/mt8189/libmtkcam_grallocutils.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V5-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    (
        'vendor/lib/mt8189/libpqconfig.so',
        'vendor/lib64/mt8189/libpqconfig.so',
    ): blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),
    'vendor/lib64/mt8189/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V2-ndk.so', 'android.hardware.camera.common-V1-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'mt8189-common',
    'mediatek',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
