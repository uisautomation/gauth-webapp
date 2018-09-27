#!/usr/bin/env bash
#
# Wrapper script to run test-suite within docker image. Arguments to the script
# are passed to tox.

# Change to this script's directory
cd "$( dirname "${BASH_SOURCE[0]}")"

# Run test suite
exec ./compose.sh tox run --rm tox $@
