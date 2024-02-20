import subprocess
from pathlib import Path

# Make sure not to import rich here, since it's an optional dependency
# Some tests assert behaviour that's predicated on it not yet being imported


# @pytest.mark.parametrize(
#     "args", [[sys.executable, "-m", "typeshed_stats"], ["typeshed-stats"]]
# )
def test_running_from_command_line(complete_typeshed: Path, args: list[str]) -> None:
    subprocess.run(["echo", "$PATH"])
    subprocess.run(["typeshed-stats"])
    # result = subprocess.run([*args, "--typeshed-dir", str(complete_typeshed)])
    # code = result.returncode
    # assert code == 0
    # result2 = subprocess.run([*args, "--help"])
    # code = result2.returncode
    # assert code == 0
