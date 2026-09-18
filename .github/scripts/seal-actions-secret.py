"""Seal a generated PFX directly to this repository's Actions public key.

The output is safe to retain in the workflow log: GitHub can decrypt the
ciphertext only after it is submitted to the Actions secrets API.
"""

import base64
import json
import os
import sys
import urllib.request

from nacl.public import PublicKey, SealedBox


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: seal-actions-secret.py CERTIFICATE.pfx")

    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/actions/secrets/public-key",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        public_key = json.load(response)

    with open(sys.argv[1], "rb") as pfx_file:
        secret_value = base64.b64encode(pfx_file.read())

    sealed_box = SealedBox(PublicKey(base64.b64decode(public_key["key"])))
    encrypted_value = base64.b64encode(sealed_box.encrypt(secret_value)).decode("ascii")
    payload = {"key_id": public_key["key_id"], "encrypted_value": encrypted_value}
    output_path = os.environ.get("SEALED_ACTIONS_SECRET_OUTPUT")
    if not output_path:
        raise SystemExit("SEALED_ACTIONS_SECRET_OUTPUT is required")
    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(payload, output_file, separators=(",", ":"))
    print(f"Signing certificate sealed for repository key {public_key['key_id']}")


if __name__ == "__main__":
    main()
