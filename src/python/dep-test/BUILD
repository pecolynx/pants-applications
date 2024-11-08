poetry_requirements(
    name="poetry",
    resolve="dep_test",
)

python_sources(
    name="src",
    resolve="dep_test",
    interpreter_constraints=["CPython>=3.9"],
    sources=["dep_test/**/*.py"],
    dependencies=[
        "src/python/lib-pydantic-v1:dep_test_src",
    ],
)

pex_binary(
    name="dep_test",
    resolve="dep_test",
    interpreter_constraints=["CPython>=3.9"],
    entry_point="dep_test/main.py",
)

python_tests(name="tests", resolve="dep_test", sources=["tests/**/*_test.py"], dependencies=[])
