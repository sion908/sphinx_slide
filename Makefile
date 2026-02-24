# Makefile configuration
SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
REVEALJSDIR   = $(BUILDDIR)/revealjs

# List of presentations
PRESENTATIONS = none 260223_ailt

# PWA icon sizes to generate (resize_icons.py で使用)
PWA_VENV      = /tmp/pwa_icon_venv
PWA_PYTHON    = $(PWA_VENV)/bin/python

.PHONY: help Makefile all-slides clean-all pwa-icons $(PRESENTATIONS)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build a specific presentation
$(PRESENTATIONS):
	@echo "Building $@..."
	@$(SPHINXBUILD) -M revealjs "$(SOURCEDIR)/slides/$@" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)
	@mkdir -p $(REVEALJSDIR)/$@
	@cp -r $(BUILDDIR)/$@/revealjs/* $(REVEALJSDIR)/$@/

# Build the top-level index (HTML)
top-index:
	@echo "Building top-level index..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/top" $(SPHINXOPTS) $(O)
	@mkdir -p $(REVEALJSDIR)
	@cp -r $(BUILDDIR)/top/html/* $(REVEALJSDIR)/
	@mkdir -p $(REVEALJSDIR)/slides/shared
	@cp -r $(SOURCEDIR)/slides/shared/_image $(REVEALJSDIR)/slides/shared/
	@cp -r $(SOURCEDIR)/slides/shared/_static $(REVEALJSDIR)/slides/shared/
	@echo "Copying PWA files to dist..."
	@cp $(SOURCEDIR)/_static/manifest.json $(REVEALJSDIR)/manifest.json
	@mkdir -p $(REVEALJSDIR)/icons
	@cp -r $(SOURCEDIR)/_static/icons/* $(REVEALJSDIR)/icons/

# PWA用アイコン生成（/tmp の仮想環境で Pillow を使ってリサイズ）
pwa-icons:
	@echo "Setting up temporary venv for icon generation..."
	@if [ ! -f "$(PWA_PYTHON)" ]; then \
		python3 -m venv $(PWA_VENV) && \
		$(PWA_VENV)/bin/pip install pillow -q; \
	fi
	@echo "Generating PWA icons..."
	@$(PWA_PYTHON) resize_icons.py image.png $(SOURCEDIR)/_static/icons/
	@echo "PWA icons generated."

# Build everything
all-slides: pwa-icons $(PRESENTATIONS) top-index
	@echo "All presentations and top-index built in $(REVEALJSDIR)"

# Clean all builds
clean-all:
	@rm -rf $(BUILDDIR)/*
	@echo "All builds cleaned."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
