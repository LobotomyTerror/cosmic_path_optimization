PROGRAM = python3
MAIN = cosmic.py
TEST = test_cosmic.py
KATTIS = kattis -p cosmicpathoptimization
UNIT_TEST = pytest
STYLE_CHECK = flake8
AUTO_FIX = autopep8 --in-place --recursive --aggressive --aggressive
TYPE_CHECK = mypy --strict

all: localtest unittest stylecheck fixstyles typecheck clean kattis

localtest:
	@cat 1.in | ${PROGRAM} ${MAIN} | diff - 1.ans

unittest:
	@${UNIT_TEST} .

stylecheck:
	@${STYLE_CHECK} .

fixstyles:
	@${AUTO_FIX} .

typecheck:
	@${TYPE_CHECK} .

clean:
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache

kattis:
	${KATTIS} ${MAIN}