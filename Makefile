# Makefile — task runner.
#
# This repo is a book. There is no package, no runtime, and no test suite yet.
# Targets are added when something real needs running, not in advance.
#
# `validate` checks gen/concepts/ frontmatter and prose rules.
# It is stdlib-only Python, so it needs no toolchain setup.

.DEFAULT_GOAL := help
.PHONY: help lint format validate

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-9s\033[0m %s\n", $$1, $$2}'

lint: ## Check markdown formatting and structure
	npx markdownlint-cli2 "**/*.md"
	npx prettier --check "**/*.md"

format: ## Apply the markdown formatter
	npx prettier --write "**/*.md"

validate: ## Validate gen/ concept files
	python3 scripts/validate-frontmatter.py
