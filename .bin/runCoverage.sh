function runCoverage () {
    coverage run --source seos/ -m pytest tests &&
    coverage html &&
    open htmlcov/index.html &&

    rm assets/coverage.svg
    coverage-badge -o assets/coverage.svg
}

runCoverage
