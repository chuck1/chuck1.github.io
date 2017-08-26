
dot_files = $(shell find _dot -name "*.dot")
png_files = $(patsubst _dot/%.dot,dot/%.png,$(dot_files))

dot/%.png: _dot/%.dot
	@mkdir -p $(dir $@)
	bash _scripts/build_dot.bash $< '-Tpng -o$@ $^'

all: $(png_files)


