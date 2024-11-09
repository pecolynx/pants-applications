poetry_requirements(
    name="poetry",
    resolve="asyncio_cpu_test",
)

python_sources(
    name="src",
    resolve="asyncio_cpu_test",
    interpreter_constraints=["CPython>=3.11"],
    sources=["asyncio_cpu_test/**/*.py"],
    dependencies=[],
)

pex_binary(
    name="asyncio_cpu_test",
    resolve="asyncio_cpu_test",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="asyncio_cpu_test/main.py",
)

python_tests(
    name="tests", resolve="asyncio_cpu_test", sources=["tests/**/*_test.py"], dependencies=[]
)
