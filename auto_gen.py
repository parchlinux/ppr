import os

archs = ("x86_64",)
base_text = """# Parch_os repo

"""
base_url = "https://github.com/parch-os/parch_repo/raw/main/{arch}/{package}"

for arch in archs:
    packages = os.listdir(arch)
    packages.sort()
    for package in packages:
        base_text += (
            "- [{}]".format(package.split(".")[0])
            + "("
            + base_url.format(arch=arch, package=package)
            + ")"
            + "\n"
        )

with open("README.md", "w") as f:
    f.write(base_text)
