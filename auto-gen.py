import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

archs = ("x86_64",)
archs_text = """[../](..)

"""
README_text = """# PPR: Parch Pacman repository

"""
base_url = "https://raw.githubusercontent.com/parchlinux/ppr/main/{arch}/{package}"

for arch in archs:
    logging.info("Generating for arch: %s", arch)
    README_text += f"- [{arch}]({arch})\n"

    packages = os.listdir(arch)
    packages.sort()

    for package in packages:
        if not ".zst" in package:
            continue

        logging.info("Generating for package: %s", package)
        archs_text += (
            f"- [{package.split('.')[0]}]"
            + "("
            + base_url.format(arch=arch, package=package)
            + ")\n"
        )

    with open(f"{arch}/README.md", "w") as f:
        f.write(archs_text)

with open("README.md", "w") as f:
    f.write(README_text)
