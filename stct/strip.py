import shutil
import tempfile
import glob
import time
import random
import subprocess

from pathlib import Path



def strip_project(project: Path, percentage: float) -> Path:
    with open(project / ".pyre_configuration", "r") as f:
        pyre_configuration = json.load(f)


def copy_project(
    original_project: Path,
    percentage: float,
    stripped_project_root: Path,
    suffix: str,
) -> Path:
    return Path(shutil.copytree(
        original_project,
        stripped_project_root / f"{original_project.name}__{percentage}_{suffix}"
    ))


def strip_types_for_project(
    project: Path,
    percentage: float,
) -> None:
    files = glob.glob(f"{project}/**/*.py", recursive=True)
    files = [f for f in files if "test" not in f]
    n_strip = int(percentage * len(files))
    to_strip = random.sample(files, n_strip)
    with open(project / "stripped_files", "w") as stripped_file_log:
        for module in to_strip:
            failures = 0
            try:
                subprocess.check_output(["strip-hints", "--inplace", module])
                stripped_file_log.write(f"{module}\n")
            except Exception:
                failures += 1
        if failures > 0:
            print(f"Failed to strip {failures} / {n_strip} files")


def copy_and_strip_project(
    original_project: Path,
    percentage: float,
    stripped_project_root: Path,
) -> None:
    t0 = time.time()
    for suffix in ["a", "b", "c", "d", "e"]:
        project = copy_project(
            original_project,
            percentage,
            stripped_project_root,
            suffix,
        )
        strip_types_for_project(
            project,
            percentage
        )
    t1 = time.time()
    print(f"Copying and stripping {project} took {t1 - t0} seconds")


def strip_types(
    projects: list[Path],
    percentages: list[float],
    stripped_project_root: Path,
) -> None:
    shutil.rmtree(stripped_project_root, ignore_errors=True)
    stripped_project_root.mkdir()
    for original_project in projects:
        for percentage in percentages:
            copy_and_strip_project(
                original_project,
                percentage,
                stripped_project_root,
            )
