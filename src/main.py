import shutil
import tempfile
import glob
import time
import random
import subprocess

from pathlib import Path



PROJECT_ROOT = Path(__file__).parent.parent
VENDORED_PROJECTS_ROOT = PROJECT_ROOT / "vendored_example_projects"
VENDORED_PROJECTS = [
    VENDORED_PROJECTS_ROOT / name
    for name in ["urllib3", "mypy", "anyio"]
]

STRIPPED_PROJECT_ROOT = PROJECT_ROOT / "stripped_examples"


def strip_project(project: Path, percentage: float) -> Path:
    with open(project / ".pyre_configuration", "r") as f:
        pyre_configuration = json.load(f)


def copy_project(
    original_project: Path,
    percentage: float,
) -> Path:
    return Path(shutil.copytree(
        original_project,
        STRIPPED_PROJECT_ROOT / f"{original_project.name}__{percentage}"
    ))


def strip_types(
    project: Path,
    percentage: float
) -> None:
    files = glob.glob(f"{project}/**/*.py")
    n_strip = int(percentage * len(files))
    to_strip = random.sample(files, n_strip)
    for module in to_strip:
        failures = 0
        try:
            subprocess.check_output(["strip-hints", "--inplace", module])
        except Exception:
            failures += 1
    if failures > 0:
        print(f"Failed to strip {failures} / {n_strip} files")


if __name__ == "__main__":
    shutil.rmtree(STRIPPED_PROJECT_ROOT, ignore_errors=True)
    STRIPPED_PROJECT_ROOT.mkdir()
    for original_project in VENDORED_PROJECTS:
        for percentage in [0.1, 0.9]:
            t0 = time.time()
            project = copy_project(original_project, percentage)
            strip_types(project, percentage)
            t1 = time.time()
            print(f"Copying and stripping {project} took {t1 - t0} seconds")
    if False:
        p = VENDORED_PROJECTS[0]
        import IPython; IPython.embed()
