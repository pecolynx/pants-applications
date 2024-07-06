poetry_requirements(
    name="poetry",
    resolve="ddtrace_app",
)

python_sources(
    name="src",
    resolve="ddtrace_app",
    interpreter_constraints=["CPython>=3.11"],
    sources=["ddtrace_app/**/*.py"],
    dependencies=[],
)

pex_binary(
    name="ddtrace_app",
    resolve="ddtrace_app",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="ddtrace_app/main.py",
)

python_tests(name="tests", resolve="ddtrace_app", sources=["tests/**/*_test.py"], dependencies=[])
