# Uso:
#  make run hello_world
#  make list

SHELL := /bin/bash
LISTAS_DIR := .

.PHONY: run list

run:
	@bin="$(filter-out $@,$(MAKECMDGOALS))"; \
	if [ -z "$$bin" ]; then \
		echo "Uso: make run <nome_do_bin>"; exit 1; \
	fi; \
	path=$$(find $(LISTAS_DIR) -type f -name "$${bin}.rs" | head -n1); \
	if [ -z "$$path" ]; then \
		echo "Arquivo '$${bin}.rs' não encontrado em $(LISTAS_DIR)/"; exit 1; \
	fi; \
	dir=$$(dirname "$$path"); \
	while [ "$$dir" != "/" ] && [ ! -f "$$dir/Cargo.toml" ]; do \
		dir=$$(dirname "$$dir"); \
	done; \
	if [ ! -f "$$dir/Cargo.toml" ]; then \
		echo "Não foi possível localizar Cargo.toml para '$$path'"; exit 1; \
	fi; \
	package=$$(basename "$$dir"); \
	cargo run --quiet -p $$package --bin $$bin

list:
	@find $(LISTAS_DIR) -type f -name "*.rs" -printf "%f\n" | sed 's/\.rs$$//' | sort

%:
	@:
