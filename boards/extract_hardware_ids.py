import json
import pathlib
from dis import pretty_flags

if __name__ == "__main__":

    usb = []

    for file in pathlib.Path(__file__).parent.glob("*.json"):
        data = json.loads(file.read_bytes())
        hwids = data.get("build", {}).get("hwids", [])

        for vid, pid in hwids:
            usb.append(
                {
                    # "_name": data["name"],
                    "vid": vid.removeprefix("0x").upper(),
                    "pid": pid.removeprefix("0x").upper(),
                }
            )

    print(json.dumps(usb, indent=True))
