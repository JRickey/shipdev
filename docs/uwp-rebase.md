# Shipwright 9.2.3 UWP rebase

This branch replays the Xbox/UWP integration from `worleydl/shipdev` onto
Shipwright 9.2.3. The working package uses a separate identity,
`ShipwrightRebased`, so it can be installed beside the known-good 9.1.0 port.

The upstream 9.2.3 `libultraship` revision remains recorded as the submodule
commit. The seven small UWP changes are kept as patches in
`patches/libultraship-uwp/` and applied by the Windows build. This avoids
depending on an unpublished libultraship fork.

The build downloads the official 9.2.3 Windows release, verifies its published
SHA-256 digest, and packages the matching `soh.o2r`. User-generated `oot.o2r`,
saves, and mods continue to live under the external `E:\soh` directory.
