# Makefile configuration
SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
REVEALJSDIR   = $(BUILDDIR)/revealjs

# List of presentations
PRESENTATIONS = presentation1 presentation2

.PHONY: help Makefile all-slides clean-all $(PRESENTATIONS)

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

# Build everything
all-slides: $(PRESENTATIONS) top-index
	@echo "All presentations and top-index built in $(REVEALJSDIR)"

# Clean all builds
clean-all:
	@rm -rf $(BUILDDIR)/*
	@echo "All builds cleaned."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
