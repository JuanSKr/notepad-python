# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MainWindow.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\\\Users\\\\Skrript\\\\Desktop\\\\Code\\\\DAM\\\\SEGUNDO\\\\Desarrollo de interfaces\\\\Ejercicios\\\\EditorDeTextos\\\\resources\\\\img\\\\abrir.png', 'resources/img'), ('C:\\\\Users\\\\Skrript\\\\Desktop\\\\Code\\\\DAM\\\\SEGUNDO\\\\Desarrollo de interfaces\\\\Ejercicios\\\\EditorDeTextos\\\\resources\\\\img\\\\guardar_como.png', 'resources/img'), ('C:\\\\Users\\\\Skrript\\\\Desktop\\\\Code\\\\DAM\\\\SEGUNDO\\\\Desarrollo de interfaces\\\\Ejercicios\\\\EditorDeTextos\\\\resources\\\\img\\\\guardar.png', 'resources/img'), ('C:\\\\Users\\\\Skrript\\\\Desktop\\\\Code\\\\DAM\\\\SEGUNDO\\\\Desarrollo de interfaces\\\\Ejercicios\\\\EditorDeTextos\\\\resources\\\\img\\\\salir.png', 'resources/img'), ('C:\\\\Users\\\\Skrript\\\\Desktop\\\\Code\\\\DAM\\\\SEGUNDO\\\\Desarrollo de interfaces\\\\Ejercicios\\\\EditorDeTextos\\\\resources\\\\styles\\\\style.qss', 'resources/styles')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MainWindow',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Skrript\\Downloads\\Icon-notepad.ico'],
)
