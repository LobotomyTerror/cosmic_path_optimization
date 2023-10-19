TEST = pytest 
TEST_ARGS = --verbose --color=yes
TYPE_CHECK = mypy --strict
STYLE_CHECK = flake8
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive
SEARCH = -find . -type d \( -name __pycache__ -o -name .mypy_cache -o -name .pytest_cache -o -name .hypothesis \) -exec rm -rf {} \; 2>/dev/null || true

.PHONY: all
all: style-check type-check run-test clean

.PHONY: type-check
type-check:
	$(TYPE_CHECK) .

.PHONY: style-check
style-check:
	$(STYLE_CHECK) .

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) .

.PHONY: clean
clean:
	@$(SEARCH)

.PHONY: push
push: run-test clean
	

.PHONY: fix-style
fix-style:
	$(STYLE_FIX) .
