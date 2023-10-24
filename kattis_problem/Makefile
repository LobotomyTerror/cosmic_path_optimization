PROGRAM = python3
MAIN = cosmic.py
TEST = test_cosmic.py
KATTIS = kattis -p cosmicpathoptimization
UNIT_TEST = pytest
STYLE_CHECK = flake8
AUTO_FIX = autopep8 --in-place --recursive --aggressive --aggressive
TYPE_CHECK = mypy --strict
CLEANALL = find . -type d \( -name __pycache__ -o -name .mypy_cache -o -name .pytest_cache -o -name .DS_Store \) -exec rm -rf {} \; 2>/dev/null || true

all: localtest unittest stylecheck fixstyles typecheck clean kattis

.PHONY: localtest
localtest:
	@cat 1.in | ${PROGRAM} ${MAIN} | diff - 1.ans

.PHONY: unittest
unittest:
	@${UNIT_TEST} .

.PHONY: stylecheck
stylecheck:
	@${STYLE_CHECK} .

.PHONY: fixstyles
fixstyles:
	@${AUTO_FIX} .

.PHONY: typecheck
typecheck:
	@${TYPE_CHECK} .

.PHONY: clean
clean:
	@$(CLEANALL)

.PHONY: kattis
kattis:
	${KATTIS} ${MAIN}
