import subprocess

MYPY_PRIMER_URL: str = "https://github.com/hauntsaninja/mypy_primer"

def git_clone(url: str) -> None:
    print(f"Cloning {url}...")
    subprocess.check_output(
        ["git", "clone", url]
    )

git_clone(MYPY_PRIMER_URL)


# lazy import, because until the clone above happens this code won't exist!
from mypy_primer import mypy_primer

for project in mypy_primer.PROJECTS:
    if project.location != MYPY_PRIMER_URL:
        git_clone(project.location)
