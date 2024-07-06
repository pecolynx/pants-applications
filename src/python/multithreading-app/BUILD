poetry_requirements(
    name="poetry",
    resolve="multithreading_app",
)

python_sources(
    name="src",
    resolve="multithreading_app",
    interpreter_constraints=["CPython>=3.11"],
    sources=["multithreading_app/**/*.py"],
    dependencies=[
        ":poetry",
    ],
)

python_tests(
    name="tests",
    resolve="multithreading_app",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[],
    skip_mypy=True,
)

pex_binary(
    name="multithreading_app",
    resolve="multithreading_app",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="multithreading_app/main.py",
    dependencies=[
        ":src",
        ":poetry",
    ],
)
