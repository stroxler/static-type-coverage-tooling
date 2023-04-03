import glob
import libcst

from pathlib import Path


class AnnotationCollector(libcst.CSTVisitor):
    path: str = ""

    def __init__(self) -> None:
        self.n_functions: int = 0
        self.n_parameters: int = 0
        self.n_returns: int = 0

    def visit_FunctionDef(self, node: libcst.FunctionDef) -> None:
        self.n_functions += 1

    @staticmethod
    def count_annotations(module_path: str) -> int:
        with open(module_path, "r") as f:
            code = f.read()
        try:
            module = libcst.parse_module(code)
            visitor = AnnotationCollector()
            module.visit(visitor)
            return visitor.n_functions
        except Exception:
            print(f"  (skipped {module_path} due to parse error)")
            return 0


def count_infer_output_on_project(project: Path) -> None:
    stubs_directory = project / ".pyre" / "types"
    stub_files = glob.glob(f"{stubs_directory}/**/*.pyi", recursive=True)
    n_functions = 0
    for stub_file in stub_files:
        n_functions += AnnotationCollector.count_annotations(stub_file)
    print(f"On project {project}:")
    print(f"  n_functions is {n_functions}, for an average of {n_functions / len(stub_files)} per module")


def count_infer_output_on_stripped_projects(
    stripped_project_root: Path,
) -> None:
    for stripped_project in stripped_project_root.iterdir():
        count_infer_output_on_project(stripped_project)
