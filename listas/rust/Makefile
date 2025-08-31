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
	start=$$(date +%s%N); \
	cargo run --quiet -p $$package --bin $$bin; \
	status=$$?; \
	end=$$(date +%s%N); \
	elapsed_ns=$$((end - start)); \
	elapsed_ms=$$((elapsed_ns / 1000000)); \
	printf "⏱️  Tempo de execução: %d.%03ds\n" $$((elapsed_ms/1000)) $$((elapsed_ms%1000)); \
	exit $$status

list:
	@find $(LISTAS_DIR) -type f -name "*.rs" -printf "%f\n" | sed 's/\.rs$$//' | sort

%:
	@:
