import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("B4_sklearn_tree_test_b4", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_accuracy_high():
    acc = starter.train(plot=False)
    assert isinstance(acc, float)
    assert acc > 0.85, f"accuracy too low: {acc}"


def test_plot_creates_file(tmp_path):
    out = str(tmp_path / "p.png")
    acc = starter.train(plot=True, out_path=out)
    assert os.path.exists(out)


# Try changing: modify this file and re-run the tests.
