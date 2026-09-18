# Ship of Harkinian UWP

This branch carries the Xbox/UWP integration on Shipwright 9.2.3. The package
uses the stable identity `ShipOfHarkinian` and the user-facing name
`Ship of Harkinian`.

The upstream 9.2.3 `libultraship` revision remains recorded as the submodule
commit. The seven small UWP changes are kept as patches in
`patches/libultraship-uwp/` and applied by the Windows build. This avoids
depending on an unpublished libultraship fork.

The build downloads the official 9.2.3 Windows release, verifies its published
SHA-256 digest, and packages the matching `soh.o2r`. User-generated `oot.o2r`,
saves, and mods continue to live under the external `E:\soh` directory.
