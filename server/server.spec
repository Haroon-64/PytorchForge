# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['modules/main.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('modules', 'modules'), ('pyproject.toml', '.')],
    hiddenimports=['fastapi', 'fastapi.middleware.cors', 'fastapi.middleware.httpsredirect', 'fastapi.middleware.trustedhost', 'uvicorn', 'uvicorn.logging', 'uvicorn.loops.auto', 'uvicorn.protocols.http.auto', 'uvicorn.protocols.websockets.auto', 'uvicorn.lifespan.on', 'pydantic', 'configs.registries.optimizerreg', 'configs.registries.lossreg', 'configs.registries.metricreg', 'configs.registries.layerreg', 'configs.registries.modelreg'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
