import shutil
import tempfile
import glob
import time
import random
import subprocess

from pathlib import Path



def run_pyre_infer_on_project(project: Path) -> None:
    print(f"Running pyre infer on {project}...")
    with open(project / "stripped_files", "r") as f:
        stripped_files = f.read().strip().split("\n")
    subprocess.check_output(
        ["pyre", "infer", *stripped_files],
        cwd=project,
    )


def run_pyre_infer_on_stripped_projects(
    stripped_project_root: Path,
) -> None:
    for stripped_project in stripped_project_root.iterdir():
        run_pyre_infer_on_project(stripped_project)
